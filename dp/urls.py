from django.conf.urls import patterns, url
from .views import AuthorCreate, Thanks, BookCreate

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^author_create/', AuthorCreate.as_view(), name='author_add'),
	url(r'^book_create/(?P<author_id>\d+)/$', BookCreate.as_view(), name='book_create'),
	url(r'^thanks/', Thanks.as_view(), name='thanks'),
	)