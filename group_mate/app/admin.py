from django.contrib import admin

# Register your models here.
from .models import Schools, Messages, Classes, User

admin.site.register(Schools)
admin.site.register(Messages)
admin.site.register(Classes)
admin.site.register(User)
