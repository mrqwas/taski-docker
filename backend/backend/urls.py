from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# noqa I004
from api import views # noqa I001

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
