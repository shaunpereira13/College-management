from django.urls import path
from .import views
from homepage import urls
urlpatterns=[
   path('studentdet/<roll_no>/',views.studentdetails,name='studentdetails'),
   path('teacherdet/<trno>/',views.teacherdetails,name='teacherdetails'),
   path('login/', views.logouts, name="Logout"),
   path('marks/<subid>/',views.marks,name='marks'),
   path('delmarks/<subid>/',views.deletestudent,name='delmarks'),
   path('createstudent/', views.createstud, name='createstudent'),
   path('updatemarks/<pk>/', views.updatemarks, name='updatemarks'),
   
]
