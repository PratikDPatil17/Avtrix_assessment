from rest_framework.pagination import PageNumberPagination
# Create your views here.

class ChangePaginationProperties(PageNumberPagination):
	page_size = 5
    page_query_param = "onpage"