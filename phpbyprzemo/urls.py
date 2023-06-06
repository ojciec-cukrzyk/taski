from django.urls.conf import path

from . import views

from django.contrib import admin
from django.urls import path, include
from .views import UserSignup,UserLogin,PersonCreate,PersonList,PersonDetail, PersonUpdate, PersonDelete, TaskEdit
from django.contrib.auth.views import LogoutView

urlpatterns = [

    #path('app/',include('djangoProject.urls')),
    #path('',views.index,name='index'),
    path('pracownicy/<int:pracownicy_id>',views.pracownicy_by_id, name="pracownicy_by_id"),
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('person-create/', PersonCreate.as_view(), name='personcreate'),
    path('', PersonList.as_view(), name='personlist'),
    path('person-detail/pk=<int:pk>', PersonDetail.as_view(), name='persondetail'),
    path('person-update/pk=<int:pk>', PersonUpdate.as_view(), name='personupdate'),
    path('person-delete/pk=<int:pk>', PersonDelete.as_view(), name='persondelete'),
    path('task-edit/pk=<int:pk>', TaskEdit.as_view(), name='taskedit'),
]