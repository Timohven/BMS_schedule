from django import forms
#from datetimepicker.widgets import DateTimePicker
#from datetimewidget.widgets import DateTimeWidget
from django.contrib.admin import widgets
from django.forms.fields import DateTimeField
from django.forms.fields import DateField

from schedule.models import Schedule, Student

# class SampleForm(forms.Form):
#     #datatime = None
#     datetime = forms.DateTimeField(widget=DateTimePicker())

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['contract', 'time', 'duration', 'office', 'type', 'state']
        labels = {'contract': 'Контракт', 'time': 'Дата и время проведения', 'duration': 'Длительность',
                  'office': 'Кабинет', 'type': 'Тип занятия', 'state': 'Статус'}
        #widgets = {'time': forms.widgets.SplitDateTimeWidget(attrs={'data_attrs': '%d.%m.%Y', 'time_attrs': '%H:%M'})}
        time = DateTimeField(widget=widgets.AdminDateWidget())
        #datetime = forms.DateTimeField(widget=DateTimePicker(script_tag=False))
        #widgets = {'time': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n=True, bootstrap_version=3)}

class StudentForm(forms.ModelForm):
    birthday = forms.DateField(widget=widgets.AdminDateWidget())
    class Meta:
        model = Student
        fields = ['surname', 'name', 'birthday']
        labels = {'surname': 'Фамилия', 'name': 'Имя', 'birthday': 'Дата рождения'}
        #bithday = DateField(widget=widgets.AdminDateWidget())