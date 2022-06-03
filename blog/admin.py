from django.contrib import admin

# Register your models here.
#5. Add to admin

from .models import (Blog)

admin.site.register(Blog)
