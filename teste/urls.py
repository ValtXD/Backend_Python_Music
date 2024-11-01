from rest_framework import routers
from teste import viewsets

router = routers.DefaultRouter()
router.register('author', viewsets.AuthorViewSet)
router.register('album', viewsets.AlbumViewSet)
router.register('music', viewsets.MusicViewSet)
urlpatterns = router.urls

