from django.contrib import admin

from .models import Rotator
from .models import RotatorLink

admin.site.register(Rotator)
admin.site.register(RotatorLink)