from rest_framework import serializers, viewsets, routers


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'

class NewsItemViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

router = routers.DefaultRouter()
router.register(r'api/news', NewsItemViewSet)

urlpatterns = [
    # ... other URL patterns ...
    path('api/', include(router.urls)),
]
