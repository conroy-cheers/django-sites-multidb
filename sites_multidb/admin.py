from django.contrib import admin
from .forms import DBConfigForm


class DBConfigAdmin(admin.ModelAdmin):
    form = DBConfigForm
