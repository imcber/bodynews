
from django.conf.urls import url
from django.contrib import admin
from posts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', views.ListView.as_view(), name="lista"),
    url(r'^crearPost/', views.CreatePostView.as_view(), name="lista"),
]
