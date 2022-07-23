from datetime import datetime, timedelta
from isoweek import Week
from django.shortcuts import render, redirect
from schedule.models import Teacher, Student, Contract, Office, Schedule, Day, Hour
from schedule.forms import ScheduleForm, StudentForm
from import_DB import clone_week

CURRENT_WEEK = datetime.today().isocalendar()[1]
CURRENT_DAY = datetime.today().isocalendar()[2]
CURRENT_MONDAY = datetime.today()-timedelta(days=CURRENT_DAY-1)
CURRENT_MONDAY = CURRENT_MONDAY.replace(hour=0, minute=0)
CURRENT_SUNDAY = CURRENT_MONDAY + timedelta(days=6)
CURRENT_SUNDAY = CURRENT_SUNDAY.replace(hour=23, minute=59)


def index(request):
    print("CURRENT_MONDAY={}, CURRENT_SUNDAY={}".format(CURRENT_MONDAY, CURRENT_SUNDAY))
    context = {'current_week': CURRENT_WEEK}
    return render(request, 'index.html', context)

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

def schedule_main(request, cur_week=CURRENT_WEEK):
    print("input week:", cur_week)
    week = int(cur_week)
    if week == 0:
        week = CURRENT_WEEK
    if week > Week.last_week_of_year(2022).week:
        week = CURRENT_WEEK
    prev_week = week - 1
    next_week = week + 1
    cur_mon = Week(2022, week).monday()
    cur_sun = Week(2022, week+1).monday()
    print("диапазон=",cur_mon,"-",cur_sun)
    schedules = Schedule.objects.filter(time__range=[cur_mon, cur_sun])
    print([cur_mon, cur_sun])
    print(schedules)
    contracts = Contract.objects.all()
    offices = Office.objects.all()
    hours = Hour.objects.all()
    days = Day.objects.all()
    context = {'schedules': schedules, 'contracts': contracts, 'offices': offices, 'hours': hours, 'days': days,
               'cur_week': week, 'prev_week': prev_week, 'next_week': next_week}
    return render(request, 'schedules.html', context)

def clone_next_week(request):
    #schedules = Schedule.objects.filter(time__range=[CURRENT_MONDAY, CURRENT_SUNDAY])
    #for schedule in schedules:
    clone_week(CURRENT_MONDAY, CURRENT_SUNDAY)

    # context = {'schedules': schedules, 'contracts': contracts, 'offices': offices, 'hours': hours, 'days': days,
    #            'cur_week': week, 'prev_week': prev_week, 'next_week': next_week}
    context = {'current_week': CURRENT_WEEK}
    return render(request, 'index.html', context)

def edit_schedule(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    p = '/another_week/' + str(schedule.time.isocalendar()[1]) + '/'
    if request.method == 'POST':
        print('POST')
        if request.POST.get("del"):
            print('DELETED')
            schedule.delete()
            return redirect(p)
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            print('CHANGED')
            form.save()
            return redirect(p)
        else:
            print('ERROR, NOT CHANGED')
            context = {'form': form}
            return render(request, 'edit_schedule.html', context)
    else:
        print('NOT CHANGED')
        form = ScheduleForm(instance=schedule)
        context = {'form': form}
        return render(request, 'edit_schedule.html', context)

def add_time_schedule(request, timeplace):
    #print("timeplace=(",timeplace,")")
    list_of_timeplace = timeplace.split()
    dayy = list_of_timeplace[0]
    hour = list_of_timeplace[1]
    off = list_of_timeplace[2]
    cur_week = int(list_of_timeplace[3])
    #day = timeplace[1:3]
    #hour = timeplace[4:9]
    #off = timeplace[10:-1]
    #print(day,' ',hour,' ',off,' ',week)
    schedule = Schedule()
    schedule.duration = 1
    offices = Office.objects.all()
    for office in offices:
        if office.get_name_display() == off:
            schedule.office=office
    hour=hour[0:2]+':00:00'
    days = Day.objects.all()
    for day in days:
        if day.get_name_display() == dayy:
            print(day.pk)
            n = day.pk - 1
    m = Week(2022, cur_week).monday()
    print('mon:',m)
    m = m + timedelta(days=n)
    print('cur:',m)
    #schedule.time = '20.07.2020 '+hour
    schedule.time = m.strftime('%d.%m.%Y')+' '+hour
    #schedule.time =
    #form = ScheduleForm(instance=schedule)
    p = '/another_week/' + list_of_timeplace[3] + '/'
    if request.method == 'POST':
        if request.POST.get("del"):
            print('nothing creating')
            return redirect(p)
        form = ScheduleForm(data=request.POST)
        print('POST')
        if form.is_valid():
            form.save()
            return redirect(p)
    else:
        form = ScheduleForm(instance=schedule)

    context = {'form': form}
    return render(request, 'edit_schedule.html', context)

def add_student(request):
    if request.method != 'POST':
        print('POST')
        form = StudentForm()
    else:
        """
        if request.POST.get("del"):
            print('nothing creating')
            return redirect('/schedule/')
        """
        form = StudentForm(data=request.POST)
        if form.is_valid():
            print('VALID')
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'edit_student.html', context)

def add_schedule(request):
    if request.method != 'POST':
        print('POST')
        form = ScheduleForm()
    else:
        if request.POST.get("del"):
            print('nothing creating')
            return redirect('/schedule/')
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            print('VALID')
            form.save()
            return redirect('/schedule/')
    context = {'form': form}
    return render(request, 'edit_schedule.html', context)










