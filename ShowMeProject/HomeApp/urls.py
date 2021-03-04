from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage, name='home'),
    path('watching/', views.WatchApp, name='Watch'),
    path('user_details/<usr_id>', views.user_details, name='user_details'),
    path('user_details_video/<usr_id>', views.user_details_video, name='user_details_video'),
    path('video_like/<likeid>', views.video_like_fun, name='video_like'),
    path('video_dislike/<dislikeid>', views.video_dislike_fun, name='video_dislike'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
