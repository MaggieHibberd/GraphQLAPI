import graphene
from graphene_django import DjangoObjectType
from .models import Book


class BooksType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'excerpt')


class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)


schema = graphene.Schema(query=Query)

