from django.urls import path, include
from rest_framework import routers

from shnk_app.views import PodsystemViewSet, GroupsViewSet, DocumentTypesViewSet, DocumentFilesViewSet, DocumentViewSet

router = routers.DefaultRouter()

router.register(r'podsystem', PodsystemViewSet)
router.register(r'groups', GroupsViewSet)
router.register(r'document-types', DocumentTypesViewSet)
router.register(r'document-files', DocumentFilesViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]