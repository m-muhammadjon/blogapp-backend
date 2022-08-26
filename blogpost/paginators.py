from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberWithLimitPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100
    page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "page_size": self.get_page_size(self.request),
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "page_items": len(self.page),
                "total": self.page.paginator.count,
                "results": data,
            }
        )

    def get_page_size(self, request):
        try:
            page_size = int(request.query_params[self.page_size_query_param])
            if page_size <= 0 or page_size > self.max_page_size:
                raise ValueError
            return page_size
        except (KeyError, ValueError):
            pass
        return self.page_size