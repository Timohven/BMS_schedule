"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from schedule.views import index, teachers_view, students_by_teacher, schedule_main, add_schedule, edit_schedule, add_time_schedule, add_student, clone_next_week

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('teachers/', teachers_view),
#оба варианта рабочие
    path('students_by_teacher/<int:teach_id>/', students_by_teacher),
#    re_path(r'students_by_teacher/(?P<teach_id>\d{1,2})/', students_by_teacher),
#обрабатывает так же вариант с незаданным индексом
#    re_path(r'students_by_teacher/(?:(?P<teach_id>\d{1,2})/)?', students_by_teacher),
#    re_path(r'students_by_teacher/(?:\teach_id=(?P<teach_id>\d{1,2})/)?', students_by_teacher),
    path('schedule/', schedule_main),
    path('editing/', admin.site.urls),
    #path('add_schedule/', add_schedule),
    path('schedule/<int:schedule_id>/', edit_schedule),
    path('add_time_schedule/<str:timeplace>/', add_time_schedule),
    #path('add_student/', add_student),
    path('another_week/<int:cur_week>/', schedule_main),
    path('clone_next_week/', clone_next_week),
]
