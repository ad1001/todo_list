from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("",include("list_app.urls")),
    path('admin/', admin.site.urls),
]
