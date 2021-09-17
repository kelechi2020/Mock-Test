import django_filters
from social import models


class PostFilterset(django_filters.FilterSet):
    class Meta:
        model = models.Post
        fields = '__all__'
