from django.contrib import admin
from .models import Survey

# Register your models here.
class SurveyAdmin(admin.ModelAdmin):    
    list_display = ('id', 'survey_name', 'pub_date', 'end_date', 'survey_description')
    list_display_links = ('id', 'survey_name')
    search_fields = ('id', 'survey_name', 'survey_description')
    list_editable = ('survey_description',)
    list_filter = ('survey_description',)

admin.site.register(Survey, SurveyAdmin)