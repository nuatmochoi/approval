from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .views import profile, IndexView,signup,tag_button
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt




app_name='dj'
urlpatterns = [

    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',signup,name='signup'),
    path('tag_button/',views.tag_button,name='tag_button'),
    path('tag_list/',views.tag_list,name='tag_list'),
    #url(r'upload_doc',views.upload_doc,name='upload_doc'),
    path('upload_doc/', views.model_form_upload, name='upload_doc'),
    #path('upload_doc/', views.upload_doc, name='upload_doc'),
    path('download_doc/',views.download,name='download_doc'),
    path('mail_li/',views.mail_li,name='mail_li'),
    path('mail_li/<int:pid>/',views.mail_detail,name='mail_detail'),
    path('approval_download/',views.approval_download,name='approval_download'),
    path('approve/<int:pid>/',views.approve,name='approve'),
    path('deny/<int:pid>/',views.deny,name='deny'),
    path('approve_list/',views.approve_list,name='approve_list'),
    path('approve_list/<int:pid>/',views.approve_detail,name='approve_detail'),
    path('deny_list/',views.deny_list,name='deny_list'),
    path('deny_list/<int:pid>/',views.deny_detail,name='deny_detail'),
    path('chat_list/',views.chat_list,name='chat_list'),
    path('chat_list/<int:pid>/',views.chat_detail,name='chat_detail'),
    path('document_list/',views.document_list, name='document_list'),

    path('tag_add_button/', views.tag_add_button, name = 'tag_add_button'),

    # for chat
    path('chat/',views.chat,name='chat'),
    path('chat/<room_name>/',views.room,name='room'),
    #url(r'chat^/$', views.chat, name='chat'),
    #url(r'chat/^(?P<room_name>[^/]+)/$', views.room, name='room'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)