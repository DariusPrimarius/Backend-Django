from django.urls import path
from .views import BookListView

urlpatterns = [
    path('booklist/', BookListView.as_view(),),
]