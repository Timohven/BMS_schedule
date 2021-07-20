from django.db import models

class Teacher(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateField()
    type_of_contact = models.CharField(max_length=10, default='мобильный')
    contact = models.CharField(max_length=30)
    def __str__(self):
        return u' % s % s' % (self.surname, self.name)

class Student(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateField()
    teachers = models.ManyToManyField(Teacher, through='Contract')
    type_of_contact = models.CharField(max_length=10, default='мобильный')
    contact = models.CharField(max_length=30)
    def __str__(self):
        return u' % s % s' % (self.surname, self.name)

class Contract(models.Model):
    KINDS = (
        (1, 'Piano'),
        (2, 'Clarinet'),
        (3, 'Vocals'),
        (4, 'Drums')
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kind = models.IntegerField(choices=KINDS)
    paymant_teacher = models.FloatField()
    paymant_student = models.FloatField()
    def __str__(self):
        return u' % s % s % s % s' % (self.teacher.surname, self.student.surname,
                                      self.student.name, self.get_kind_display())

class Office(models.Model):
    NAMES = (
        (1, 'Кларнет-холл'),
        (2, 'Морской'),
        (3, 'Полосатый'),
        (4, 'Зел.Дом'),
        (5, 'Конса'),
        (6, 'Барабан'),
        (7, '1_Этаж')
    )
    name = models.IntegerField(choices=NAMES)
    description = models.CharField(max_length=30)
    def __str__(self):
        return u' % s' % (self.get_name_display())

class Schedule(models.Model):
    TYPES = (
        (1, 'в школе'),
        (2, 'онлайн из школы'),
        (3, 'онлайн из дома'),
        (4, 'вне школы')
    )
    STATES = (
        (1, 'ожидается'),
        (2, 'состоялось'),
        (3, 'отменено преподавателем'),
        (4, 'отменено студентом')
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    time = models.DateTimeField()
    duration =models.FloatField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPES, default=1)
    state = models.IntegerField(choices=STATES, default=1)
    def __str__(self):
        return u' % s - % s % s \n % s/% s % s % s' % (self.contract.teacher.surname, self.contract.student.surname,
                                                 self.contract.student.name, self.time.hour, self.time.strftime("%a"),
                                                 self.get_type_display(), self.get_state_display())

class Day(models.Model):
    DAYS = (
        (0, 'ПН'),
        (1, 'ВТ'),
        (2, 'СР'),
        (3, 'ЧТ'),
        (4, 'ПТ'),
        (5, 'СБ'),
        (6, 'ВС')
    )
    name = models.IntegerField(choices=DAYS)
    def __str__(self):
        return u' % s' % (self.get_name_display())

class Hour(models.Model):
    HOURS = (
        (9, '09-10'),
        (10, '10-11'),
        (11, '11-12'),
        (12, '12-13'),
        (13, '13-14'),
        (14, '14-15'),
        (15, '15-16'),
        (16, '16-17'),
        (17, '17-18'),
        (18, '18-19'),
        (19, '19-20')
    )
    name = models.IntegerField(choices=HOURS)
    def __str__(self):
        return u' % s' % (self.get_name_display())