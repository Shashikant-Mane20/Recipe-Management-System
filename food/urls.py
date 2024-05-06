from food import views
from django.urls import path


app_name = 'food' #it is easy to for django to recognise my urls eg: food:details
urlpatterns = [
    # food/
    path('',views.index,name="index"),
    #food/item_id
    path('<int:item_id>',views.details,name="details"),
    path('item/',views.Item,name="item"),
    # path('product/',views.product,name='product'),
    # add items
    path("add",views.create_item,name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete<int:id>',views.delete_item,name='delete_item'),
]
  