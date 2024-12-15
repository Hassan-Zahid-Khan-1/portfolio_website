from django.urls import path
from portfolio.views import *


urlpatterns = [
path('portfolio/',portfolio,name='portfolio'),
 path('fullview/<int:view_id>/',fullview,name="fullview")
   
]