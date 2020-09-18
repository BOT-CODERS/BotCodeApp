from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('developers/',views.developers,name="developers"),
    path('add',views.add,name='add'),
]
