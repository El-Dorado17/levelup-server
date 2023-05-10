from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from levelupapi.views import GameTypeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

#register
# Requests to http://localhost:8000/register will be routed to the register_user function
#login
# Requests to http://localhost:8000/login will be routed to the login_user function

