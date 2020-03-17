from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from  . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.index,name='signup'),
    path('post/',views.index,name='posts'),
    path('new/post/',views.new_post, name='new_post'),
    path('profile/', views.profile, name='profile'),
    path('search/',  views.search_results, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
