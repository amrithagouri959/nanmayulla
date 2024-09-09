from django.contrib import admin
from .models import Employee, WorkSession

class WorkSessionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_time', 'end_time', 'duration', 'description')
    list_filter = ('employee', 'start_time', 'end_time')
    search_fields = ('employee__name', 'start_time', 'end_time', 'description')

    def duration(self, obj):
        return obj.duration()
    duration.short_description = 'Duration'

admin.site.register(Employee)
admin.site.register(WorkSession, WorkSessionAdmin)
