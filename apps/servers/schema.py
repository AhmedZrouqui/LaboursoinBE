import graphene
from uuid import uuid4
from graphene_django import DjangoObjectType
from .models import Server as ServerModule

class ServerNode(DjangoObjectType):
    class Meta:
        model = ServerModule
        fields = "__all__"

class CreateServer(graphene.Mutation):
    server = graphene.Field(ServerNode)

    class Arguments:
        _serverName = graphene.String()
        _buyPrice = graphene.Float()
        _sellPrice = graphene.Float()
        _serverType = graphene.String()
        _stock = graphene.Int()

    def mutate(self, info, _serverName, _buyPrice, _sellPrice, _serverType, _stock):
        newServer = ServerModule(name=_serverName,
                                buyPrice=_buyPrice,
                                sellPrice=_sellPrice,
                                serverType=_serverType,
                                stock=_stock)
        newServer.save()

        return CreateServer(server = newServer)

class UpdateServer(graphene.Mutation):
    server = graphene.Field(ServerNode)

    class Arguments:
        _serverID = graphene.UUID()
        _serverName = graphene.String()
        _buyPrice = graphene.Float()
        _sellPrice = graphene.Float()
        _serverType = graphene.String()
        _stock = graphene.Int()

    def mutate(self, info, _serverID ,_serverName, _buyPrice, _sellPrice, _serverType, _stock):

        updateServer = ServerModule.objects.get(id=_serverID)

        
        updateServer.name = _serverName
        updateServer.buyPrice = _buyPrice
        updateServer.sellPrice = _sellPrice
        updateServer.serverType = _serverType
        updateServer.stock = _stock

        updateServer.save()

        return UpdateServer(server = updateServer)

class UpdateServerStock(graphene.Mutation):
    server = graphene.Field(ServerNode)

    class Arguments:
        _serverID = graphene.UUID()
        _stock = graphene.Int()
    
    def mutate(self, info, _serverID, _stock):

        updateStock = ServerModule.objects.get(id=_serverID)

        updateStock.stock = _stock
        updateStock.save()

        return UpdateServerStock(server= updateStock)

class ServerMutation(graphene.ObjectType):

    create_server = CreateServer.Field()
    update_server = UpdateServer.Field()
    update_server_stock = UpdateServerStock.Field()

class ServerQuery(graphene.ObjectType):
    servers = graphene.List(ServerNode)
    
    def resolve_servers(self, info):
        return ServerModule.objects.all()