from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering =  'name'




# offsetpaginations
# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param ='mylimit'
#     offset_query_param ='myoffset'
#     max_limit = 5



# #local Paginations
# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 2
#     #it changes search page to p
#     page_query_param = 'p'
#     #with help of below line client can search for records
#     page_size_query_param = 'records'
#     #this will restrict number of records
#     max_page_size = 5
#     # if you want to go on last pagae you can direct write 'end'
    #   last_page_strings = 'end'