from django.contrib import admin

from myapp.models import JobPost

# Register your models here.
class jobAdmin(admin.ModelAdmin):
    list_display =('title','date','expiry')
    list_filter = ('date','salary','expiry')
    search_fields = ('title',)
    search_help_text = "Enter text to search"
    fields = ('title', 'description',"expiry")

admin.site.register(JobPost,jobAdmin)
