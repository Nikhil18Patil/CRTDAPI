from django.contrib import admin
from .models import JobCode, Register, Passkey



admin.site.register(JobCode)
admin.site.register(Register)
admin.site.register(Passkey)

# Register your models here.
