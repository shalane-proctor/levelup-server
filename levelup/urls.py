from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from levelupapi.views import check_user, register_user
from levelupapi.views import GameTypeView, GameView, EventView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
