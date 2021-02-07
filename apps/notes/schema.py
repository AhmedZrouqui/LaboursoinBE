import graphene
from uuid import uuid4
from graphene_django import DjangoObjectType
from .models import Note as NoteModule
from apps.users.models import User as UserModule

class NoteNode(DjangoObjectType):
    class Meta:
        model = NoteModule
        fields = "__all__"

class CreateNote(graphene.Mutation):
    note = graphene.Field(NoteNode)

    class Arguments:
        _userID = graphene.UUID()
        _stars = graphene.Int()
        _note = graphene.String()

    def mutate(self, info, _userID, _stars, _note):
        _user = UserModule.objects.get(uid=_userID)
        newNote = NoteModule(   user=_user,
                                stars=_stars,
                                note=_note)
        newNote.save()

        return CreateNote(note = newNote)

class UpdateNote(graphene.Mutation):
    note = graphene.Field(NoteNode)

    class Arguments:
        _noteID = graphene.UUID()
        _stars = graphene.Int()
        _note = graphene.String()

    def mutate(self, info, _noteID ,_stars, _note):

        updateNote = NoteModule.objects.get(id=_noteID)

        updateNote.star = _stars
        updateNote.note = _note

        updateNote.save()

        return UpdateNote(note = updateNode)

class DeleteNote(graphene.Mutation):
    note = graphene.Field(NoteNode)

    class Arguments:
        _noteID = graphene.UUID()
    
    def mutate(self, info, _noteID):
        deleteNote = NoteModule.objects.filter(id=_noteID)

        deleteNote.delete()


class NoteMutation(graphene.ObjectType):
    create_note = CreateNote.Field()
    update_note = UpdateNote.Field()
    delete_note = DeleteNote.Field()


class NoteQuery(graphene.ObjectType):

    notes = graphene.List(NoteNode)
    notesByUserID = graphene.List(NoteNode, uid = graphene.UUID())
    
    def resolve_notes(self, info):
        return NoteModule.objects.all()
    
    def resolve_notesByUserID(self, info, uid):
        return NoteModule.objects.filter(user=uid)
