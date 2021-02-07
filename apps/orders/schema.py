import graphene
from uuid import uuid4
from graphene_django import DjangoObjectType
from .models import Order as OrderModule
from apps.users.models import User as UserModule
from apps.servers.models import Server as ServerModule

class OrderNode(DjangoObjectType):
    class Meta:
        model = OrderModule
        fields = "__all__"

class UpdateOrder(graphene.Mutation):
    order = graphene.Field(OrderNode)
    class Arguments:
        _orderID = graphene.UUID()
        _userID = graphene.UUID()
        _serverID = graphene.UUID()
        _orderType = graphene.String()
        _quantity = graphene.Int()
        _payChoice = graphene.String()
        _amount = graphene.Float()
        _completed = graphene.Boolean()
    
    def mutate(self, info, _orderID ,_userID, _serverID, _orderType, _quantity, _payChoice, _amount, _completed):

        _order = OrderModule.objects.get(id=_orderID)
        user = UserModule.objects.get(uid=_userID)
        server = ServerModule.objects.get(id=_serverID)

        _order.user = user
        _order.server = server
        _order.orderType = _orderType
        _order.quantity = _quantity
        _order.payChoice = _payChoice
        _order.amount = _amount
        _order.completed = _completed
        _order.updated_at = timezone.now()

        _order.save()

        return UpdateOrder(order=_order)

class CreateOrder(graphene.Mutation):
    order = graphene.Field(OrderNode)

    class Arguments:
        _userID = graphene.UUID()
        _serverID = graphene.UUID()
        _orderType = graphene.String()
        _quantity = graphene.Int()
        _payChoice = graphene.String()
        _amount = graphene.Float()
        _completed = graphene.Boolean()
    
    def mutate(self, info, _userID, _serverID, _orderType, _quantity, _payChoice, _amount, _completed):
        newOrder = OrderModule(orderType=_orderType, 
                                quantity= _quantity, 
                                payChoice= _payChoice, 
                                completed =_completed, 
                                amount=_amount)

        server = ServerModule.objects.get(id=_serverID)
        user = UserModule.objects.get(uid=_userID)

        newOrder.server = server
        newOrder.user = user

        newOrder.save()
        return CreateOrder(order=newOrder)


class OrderMutation(graphene.ObjectType):

    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()


class OrderQuery(graphene.ObjectType):
    orders = graphene.List(OrderNode)
    ordersByServerID = graphene.List(OrderNode, serverID=graphene.UUID())
    ordersByServerName = graphene.List(OrderNode, serverName=graphene.String())
    ordersByUserID = graphene.List(OrderNode, uid = graphene.UUID())

    def resolve_orders(self,info):
        return OrderModule.objects.all()
    
    def resolve_ordersByServerID(self,info,serverID):
        return  OrderModule.objects.filter(server=serverID)
    
    def resolve_ordersByServerName(self, info, serverName):
        _server = ServerModule.objects.get(name=serverName)
        return OrderModule.objects.filter(server=_server)
    
    def resolve_ordersByUserID(self, info, uid):
        return OrderModule.objects.filter(user=uid)