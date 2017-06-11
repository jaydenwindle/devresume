from django.contrib import admin

from models import User, Work, Education, Skill

# Register your models here.
admin.site.register(User)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Skill)

# Allow editing of related models under user area of admin
class WorkInline(admin.StackedInline):
    model = Work
    extra = 1

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [
        WorkInline,
        EducationInline,
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
