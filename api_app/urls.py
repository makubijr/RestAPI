from rest_framework import routers
from .import views
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'students',views.StudentViewsets)
router.register(r'courses',views.CourseViewsets)

urlpatterns = [
    path('data/',include(router.urls)),
]