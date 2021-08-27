from rest_framework import routers, urlpatterns
from .api import SurveyViewSet

router = routers.DefaultRouter()
router.register('api/survey', SurveyViewSet, 'survey')

urlpatterns = router.urls