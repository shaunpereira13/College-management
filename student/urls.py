from django.urls import path
from .import views
from homepage import urls
urlpatterns=[
   path('studentdet/<roll_no>/',views.studentdetails,name='studentdetails'),
   path('teacherdet/',views.teacherdetailss,name='teacherdetails'),
   path('login/', views.logouts, name="Logout"),
   path('marks/',views.marks,name='marks'),
]
