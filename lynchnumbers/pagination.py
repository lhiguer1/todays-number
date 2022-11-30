from rest_framework.pagination import PageNumberPagination


class NumberPageNumberPagination(PageNumberPagination):
    page_size = 100
