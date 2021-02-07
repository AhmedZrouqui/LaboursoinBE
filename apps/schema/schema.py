import graphene
from uuid import uuid4
from graphene_django import DjangoObjectType
from apps.users.schema import AuthMutation,MyUserQuery
from apps.servers.schema import ServerMutation, ServerQuery
from apps.orders.schema import OrderMutation, OrderQuery
from apps.notes.schema import NoteMutation, NoteQuery


class Mutation( AuthMutation,
                ServerMutation,
                OrderMutation,
                NoteMutation,
                graphene.ObjectType):
    pass





#Query Class
class Query(MyUserQuery,
            ServerQuery,
            OrderQuery,
            NoteQuery,
            graphene.ObjectType):
    pass
    

schema = graphene.Schema(query=Query, mutation=Mutation)