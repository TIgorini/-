from django.urls import path

from . import views

app_name = 'concerts'
urlpatterns = [
	path('', views.index, name='index'),
	path('load', views.load, name='load'),
	path('create', views.create, name='create'),
	path('<int:concert_id>/remove', views.remove, name='remove'),
	path('<int:concert_id>/detail', views.detail, name='detail'),
	path('<int:concert_id>/edit', views.edit, name='edit'),
	path('logs', views.logs, name='logs'),
]