import graphene
from graphene_django.types import DjangoObjectType
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "published_year")

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        # Trả về tất cả sách
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        # Trả về một sách theo ID
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
