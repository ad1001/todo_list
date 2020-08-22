from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name = "index"),
    path("addItem/",views.addItem,name = "Add"),
    path("complete/<todo_id>",views.complete,name = "complete"),
    path("remove/",views.remove,name ="remove")
  ]
