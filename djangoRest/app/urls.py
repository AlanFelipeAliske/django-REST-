from app.views import TodoViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls