from django.contrib import admin
from .models import Escort
from .models import patient
from .models import Diseases
from .models import Medicine
from .models import Reminder
from .models import Document
from .models import Register
from .models import Login

# Register your models here.
admin.site.register(Escort)
admin.site.register(patient)
admin.site.register(Diseases)
admin.site.register(Medicine)
admin.site.register(Reminder)
admin.site.register(Document)
admin.site.register(Register)
admin.site.register(Login)