import uuid
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

user_model = get_user_model()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.IntegerField(unique=True)
    user = models.ForeignKey(user_model, on_delete=models.DO_NOTHING)
    likes_count = models.PositiveIntegerField()
    post_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
