
from django.conf.urls import url
from django.contrib import admin
from posts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', views.ListView.as_view(), name="lista"),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
