from django.urls import path  
from config import views
urlpatterns = [  
        path('signup/', views.signup, name="signup"),  
        path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
]