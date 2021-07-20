from django import forms
from datetimepicker.widgets import DateTimePicker


#from datetimewidget.widgets import DateTimeWidget
from schedule.models import Schedule

class SampleForm(forms.Form):
    datetime = forms.DateTimeField(widget=DateTimePicker())

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['contract','time','duration','office','type']
        labels = {'contract': 'Контракт','time': 'Дата и время проведения','duration': 'Длительность','office': 'Кабинет','type': 'Тип занятия'}
        # widgets = {'time': forms.widgets.SplitDateTimeWidget(attrs={'data_attrs': '%d.%m.%Y', 'time_attrs': '%H:%M'})}

        #datetime = forms.DateTimeField('time'=DateTimePicker(), )
        #widgets = {'time': DataTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)}

