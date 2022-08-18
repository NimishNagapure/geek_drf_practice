
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stdapi/', views.Nimish_API),
    path('stdapi/<int:pk>', views.Nimish_API),


]
