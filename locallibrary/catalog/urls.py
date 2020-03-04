"""
catalog/ — 홈/색인(index) 페이지.
catalog/books/ — 모든 책들의 목록.
catalog/authors/ — 모든 저자들의 목록.
catalog/book/<id> — <id> 라는 이름의(기본값) 프라이머리 키(primary key) 필드를 가지는 특정한 책을 위한 세부 사항 뷰(detail view).
                    ex) 목록에 추가된 세 번째 책은 /catalog/book/3
catalog/author/<id> —  <id> 라는 이름의 프라이머리 키(primary key) 필드를 가지는 특정한 저자를 위한 세부 사항 뷰(detail view).
                    ex) 목록에 추가된 11번째 저자는 /catalog/author/11
"""

from django.urls import path, re_path
from catalog import views

urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
     path('authors/', views.AuthorListView.as_view(), name='authors'),
     re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

