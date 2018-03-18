from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

     url('^$',views.index,name = 'landing'),
      url(r'^posts/',views.post,name = 'post'),
        url(r'^hood/',views.my_hood,name = 'my_hood'),
        url(r'^join/hood/',views.my_hood,name = 'join_hood'),
        url(r'^leave/hood/',views.my_hood,name = 'leave_hood'),
       url(r'^new/profile$', views.Profile, name='new_profile'),
       url(r'^new/post$', views.new_post, name='new_post'),


 ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
