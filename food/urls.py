from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),

    #add item
    path('add',views.CreateItem.as_view(),name='create_item'),

    #edit
    path('edit/<int:id>',views.edit_item,name='edit_item'),

    #delete
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]