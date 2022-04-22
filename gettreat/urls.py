from django.urls import path
from .import views

app_name = 'gettreat'
urlpatterns = [

# clints of =====================================
path('', views.Homeview, name="homepage"),

path('contact', views.Contactview, name="contactpage"),

path('service/', views.Serviceview, name='servicepage'),

path('about/',views.Aboutview, name="aboutpage"),

path('clients_infor/',views.Clientsview, name="clientspage"),

# end of clients=====================================


# hospital views======================================

path('indexhp/', views.Hospitaldash, name="hospitapage"),

# end of hospital view================================

path('index', views.dashboard, name="dashboardpage"),

path('hospital_datails/', views.HospitalDetails, name="hopitaldetails"),

path('emergency/', views.EmergencyRequest, name="emergencypage"),

path('login/', views.Loginview, name="loginpage"),
path('register/', views.Registeriew, name="registerpage"),
path('logout/', views.logoutUser, name="logout"),

]