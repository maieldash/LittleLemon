from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/', views.menu, name="menu"),
    path('menu/<str:itemName>', views.menuItem, name="menuItem"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)