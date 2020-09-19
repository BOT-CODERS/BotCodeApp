from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('developers/',views.developers,name="developers"),
    path('add',views.add,name='add'),
    path('404/',views.error,name='error'),
]
