from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from schedule.models import Teacher,Student,Contract,Office,Schedule,Day,Hour
from schedule.forms import ScheduleForm

def index(request):
    return render(request,'index.html')

def teachers_view(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    contracts = Contract.objects.all()
    context = {'students': students, 'teachers': teachers, 'contracts': contracts}
    return render(request, 'teachers.html', context)

def students_by_teacher(request, teach_id):
#    teach_id = request.GET["teach_id"]
    if teach_id == None:
        teach_id=1
    students = Student.objects.filter(teachers=teach_id)
    teachers = Teacher.objects.all()
    current_teacher = Teacher.objects.get(pk=teach_id)
    context = {'students': students, 'teachers': teachers, 'current_teacher': current_teacher}
    return render(request, 'by_teacher.html', context)

def schedule_main(request):
    schedules = Schedule.objects.all()
    contracts = Contract.objects.all()
    offices = Office.objects.all()
    hours = Hour.objects.all()
    days = Day.objects.all()
    context = {'schedules': schedules, 'contracts': contracts, 'offices': offices, 'hours': hours, 'days': days}
    return render(request, 'schedules.html', context)

def add_schedule(request):
    if request.method != 'POST':
        print('-1')
        form = ScheduleForm()
    else:
        print('0')
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            print('1')
            form.save()
            return redirect('/schedule/')
    print('2')
    context = {'form': form}
    return render(request, 'add_schedule.html', context)

def edit_schedule(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    if request.method == 'POST':
        print('error 0')
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            print('error 1')
            form.save()
            return redirect('/schedule/')
        else:
            print('error 2')
            context = {'form': form}
            return render(request, 'add_schedule.html', context)
    else:
        print('error 3')
        form = ScheduleForm(instance=schedule)
        context = {'form': form}
        return render(request, 'add_schedule.html', context)

def add_time_schedule(request, timeplace):
    #print(timeplace)
    day = timeplace[1:3]
    hour = timeplace[4:9]
    off = timeplace[10:]
    print(day,' ',hour,' ',off)
    schedule = Schedule()
    schedule.duration = 1
    offices = Office.objects.all()
    for office in offices:
        if office.get_name_display() == off:
            schedule.office=office
    hour=hour[0:2]+':00:00'
    print(hour)
    schedule.time = '20.07.2020 '+hour
    #form = ScheduleForm(instance=schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        print('POST')
        if form.is_valid():
            form.save()
            return redirect('/schedule/')
    else:
        form = ScheduleForm(instance=schedule)

    context = {'form': form}
    return render(request, 'add_schedule.html', context)












