from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.get,name="home"),
    path("post",views.post1,name="post1"),
    path("read",views.read_student,name="read_student"),
    path("create",views.create_student,name="create_student"),
    path("student_info/<int:id>/",views.student_info),
    path("delete_student/<int:id>/",views.delete_student),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)