from django.db import models

MESSENGERS = (
    (1, 'Viber'),
    (2, 'Telegram'),
    (3, 'WhatsApp'),
    (4, 'another')
)

KINDS = (
    (1, 'Piano'),
    (2, 'Clarinet'),
    (3, 'Vocals'),
    (4, 'Drums')
)

class Teacher(models.Model):

    surname = models.CharField(max_length=30, verbose_name=' Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    birthday = models.DateField(verbose_name='Дата рождения')
    contact = models.CharField(max_length=30, verbose_name='Номер тел')
    messenger = models.IntegerField(choices=MESSENGERS, default=1)
    comments = models.CharField(max_length=100, verbose_name='Коментарии', blank=True)

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = ''
        ordering = ['-birthday']

    def __str__(self):
        return u' % s % s' % (self.surname, self.name)

class Student(models.Model):

    surname = models.CharField(max_length=30, verbose_name=' Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    birthday = models.DateField(verbose_name='Дата рождения')
    teachers = models.ManyToManyField(Teacher, through='Contract', verbose_name='Преподаватель')
    contact = models.CharField(max_length=30, verbose_name='Номер тел')
    messenger = models.IntegerField(choices=MESSENGERS, default=1)
    source = models.CharField(max_length=30, default='АШБ', verbose_name='Источник', blank=True)
    comments = models.CharField(max_length=100, verbose_name='Коментарии', blank=True)
    agent_name = models.CharField(max_length=30, verbose_name='Имя представителя', blank=True)
    agent_type = models.CharField(max_length=30, verbose_name='Вид представителя', blank=True)
    agent_contact = models.CharField(max_length=30, verbose_name='Номер представителя', blank=True)

    class Meta:
        verbose_name_plural = 'Ученики'
        verbose_name = ''
        ordering = ['-birthday',  'surname']

    def __str__(self):
        return u' % s % s' % (self.surname, self.name)

class Contract(models.Model):

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kind = models.IntegerField(choices=KINDS)
    paymant_teacher = models.FloatField()
    paymant_student = models.FloatField()
    comments = models.CharField(max_length=100, verbose_name='Коментарии', blank=True)

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
    duration =models.FloatField(default=1)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPES, default=1)
    state = models.IntegerField(choices=STATES, default=1)

    def __str__(self):
        return u' % s - % s % s \n % s:00 % s % s % s' % (self.contract.teacher.surname, self.contract.student.surname,
                                                 self.contract.student.name, self.time.hour, self.time.strftime("%d/%m"),
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