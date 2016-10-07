from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^$', home_page, name='homepage'),
    url(r'^user-dashboard', user_dashboard, name='userdashboard'),
    

]
