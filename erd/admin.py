from django.contrib import admin
from .models import Escort
from .models import patient
from .models import Diseases
from .models import Medicine

# Register your models here.
admin.site.register(Escort)
admin.site.register(patient)
admin.site.register(Diseases)
admin.site.register(Medicine)