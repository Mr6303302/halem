from django.contrib import admin
from .models import project,main_project,project_image
# Register your models here.
admin.site.register(project)
admin.site.register(main_project)
admin.site.register(project_image)
