from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Q

from core.models import Branch
from rest_framework import status
from rest_framework.settings import api_settings
from core.serializers import BranchSerializer
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.postgres.search import SearchVector


class BranchViewSet(ViewSet, LimitOffsetPagination):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def filter_branch_by_partial_name(self, request):
        partial_name = request.query_params.get('q', None)

        branch_entities = Branch.objects.all()
        if partial_name:
            branch_entities = branch_entities.filter(
                branch__icontains=partial_name)

        page = self.paginate_queryset(branch_entities, request)

        serialized_branch_entities = BranchSerializer(page,
                                                      many=True)

        return self.get_paginated_response(serialized_branch_entities.data)

    def filter_branch_by_all(self, request):
        search_text = request.query_params.get('q', None)

        branch_entities = Branch.objects.all()

        if search_text:
            branch_entities = Branch.objects.annotate(search=SearchVector(
                'branch', 'city', 'bank__name', 'ifsc', 'address', 'district', 'state'),).filter(search=search_text)
            # branch_entities =  branch_entities.filter(
            #     Q(branch__icontains=search_text) | Q(
            #         address__icontains=search_text) | Q(ifsc__icontains=search_text)
            #     | Q(city__icontains=search_text) | Q(district__icontains=search_text)
            #     | Q(state__icontains=search_text) | Q(bank__name__icontains=search_text))

        page = self.paginate_queryset(branch_entities, request)

        serialized_branch_entities = BranchSerializer(page,
                                                      many=True)

        return self.get_paginated_response(serialized_branch_entities.data)
