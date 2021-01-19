from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('User', views.UserView)
router.register('Role', views.RoleView)
router.register('Company', views.CompanyView)
urlpatterns = [
    path('', include(router.urls))

]
