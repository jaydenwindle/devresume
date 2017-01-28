from django.contrib import admin

from models import User, SocialProfile, WorkEntry, EducationEntry, SkillEntry

# Register your models here.
admin.site.register(User)
admin.site.register(SocialProfile)
admin.site.register(WorkEntry)
admin.site.register(EducationEntry)
admin.site.register(SkillEntry)

# Allow editing of related models under user area of admin
class SocialProfileInline(admin.StackedInline):
    model = SocialProfile 
    extra = 1

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
        SocialProfileInline,
        EducationEntryInline,
        SkillEntryInline,
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
