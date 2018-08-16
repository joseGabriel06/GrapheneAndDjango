import graphene

from graphene_django.types import DjangoObjectType

from .models import Category, Mutant


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class MutantType(DjangoObjectType):
    class Meta:
        model = Mutant


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_mutants = graphene.List(MutantType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_mutants(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Mutant.objects.select_related('category').all()