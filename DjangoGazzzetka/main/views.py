from rest_framework.viewsets import ModelViewSet
from .models import Channel, Article, ArticleRelease
from .serializers import ChannelSerializer, ArticleSerializer, ArticleReleaseSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=False, methods=['get'])
    def by_channel(self, request):
        channel_id = request.query_params.get('channel_id')
        if not channel_id:
            return Response({"error": "channel_id is required"}, status=400)
        posts = self.queryset.filter(channel_id=channel_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)



class ArticleReleaseViewSet(ModelViewSet):
    queryset = ArticleRelease.objects.all()
    serializer_class = ArticleReleaseSerializer
