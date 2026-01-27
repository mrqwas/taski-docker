from django.contrib import admin # noqa I005
from django.urls import include, path # noqa I001
from rest_framework import routers # noqa I001
# noqa I004
from api import views # noqa I001

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
