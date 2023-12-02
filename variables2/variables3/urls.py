from django.urls import path

from .views import text_view

urlpatterns = [
    # path('members/', views.members, name='members'),
    #  path('home_view/',home_view,name='home_view'),
    path('text_view/',text_view,name='text_view')
]
