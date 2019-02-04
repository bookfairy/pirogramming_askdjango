import re
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError("Invalid LngLat Type")


class Post(models.Model):
    STATUC_CHOICE = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력하세요. 최대 100자.')
    content = models.TextField(verbose_name='내용', help_text='마크다운 문법을 사용해주세요.')
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d', processors=[Thumbnail(300, 300)],
                                format='JPEG', options={'quality': 60})
    lnglat = models.CharField(max_length=50, blank=True, validators=[lnglat_validator], help_text='경도, 윈도 포맷으로 입력하세요.')
    status = models.CharField(max_length=1, choices=STATUC_CHOICE)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='내용')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
