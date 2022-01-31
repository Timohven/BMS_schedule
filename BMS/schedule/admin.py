from django.contrib import admin
from schedule.models import Teacher, Student, Contract, Office, Schedule, Hour, Day

class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'birthday', 'messenger',
                    'contact', 'source', 'comments')
    list_display_links = ('surname', 'name')
    search_fields = ('surname',)

admin.site.register(Teacher)
admin.site.register(Student, StudentAdmin)
admin.site.register(Contract)
admin.site.register(Office)
admin.site.register(Schedule)
#admin.site.register(Hour)
#admin.site.register(Day)


