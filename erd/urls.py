from django.urls import path,include
from .import views 
from .views import GetPatient ,GetEscort,GetDiseases,GetDocument,GetReminder,GetMedicine,GetLogin,GetRegister
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'patient', views.GetPatient,basename='patient')
router.register(r'Escort', views.GetEscort,basename='Escort')
router.register(r'Reminder', views.GetReminder,basename='Reminder')
router.register(r'Diseases', views.GetDiseases,basename='Diseases')
router.register(r'Document', views.GetDocument,basename='Document')
router.register(r'Medicine', views.GetMedicine,basename='Medicine')
router.register(r'Login', views.GetLogin,basename='Login')
router.register(r'Register', views.GetRegister,basename='Register')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('Login/', views.GetLogin.as_view(), name='Login'),
    # path('patients/', GetPatient.as_view(), name='patient'),
    # path('escorts/', views.GetEscort.as_view(), name='Escort'),
    # path('reminders/', views.GetReminder.as_view(), name='Reminder'),
    # path('diseases/', views.GetDiseases.as_view(), name='Diseases'),
    # path('documents/', views.GetDocument.as_view(), name='Document'),
    # path('medicines/', views.GetMedicine.as_view(), name='Medicine'),
]
urlpatterns += router.urls
