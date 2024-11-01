from rest_framework import viewsets

from teste import models, serializers, filters


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filterset_class = filters.AuthorFilter


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    filterset_class = filters.AlbumFilter


class MusicViewSet(viewsets.ModelViewSet):
    queryset = models.Music.objects.all()
    serializer_class = serializers.MusicSerializer
    filterset_class = filters.MusicFilter
