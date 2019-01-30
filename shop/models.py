from django.conf import settings
from django.db import models


# blog 앱의 Post도, shop 앱의 Post도
# User(AUTH)를 외래키로 함꼐 : 이름 중복
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop_post_set')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
