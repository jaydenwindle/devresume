from django.contrib import admin

from models import User, WorkEntry, EducationEntry, SkillEntry

# Register your models here.
admin.site.register(User)
admin.site.register(WorkEntry)
admin.site.register(EducationEntry)
admin.site.register(SkillEntry)

# Allow editing of related models under user area of admin
class WorkEntryInline(admin.StackedInline):
    model = WorkEntry
    extra = 1

class EducationEntryInline(admin.StackedInline):
    model = EducationEntry
    extra = 1

class SkillEntryInline(admin.StackedInline):
    model = SkillEntry
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [
        WorkEntryInline,
        EducationEntryInline,
        SkillEntryInline,
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
