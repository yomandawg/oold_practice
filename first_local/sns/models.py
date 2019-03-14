from django.db import models

# Imagekit
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.
class Posting(models.Model):
    content = models.TextField(default='')
    icon = models.CharField(max_length=20, default='')
    # image = models.ImageField(blank=True, upload_to='postings/%Y%m%d') # 오리지널 저장용
    # Resized image
    image = ProcessedImageField(upload_to='postings/resize/%Y%m%d', processors=[ResizeToFit(width=960, upscale=False)], format='JPEG')
    # image_thumbnail 경로만 설정해놓고, 누가 호출하면 그 때 등장(cache 로 등장)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(width=320, upscale=False)], format='JPEG', options={'quality': 60})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.content[:20]}'


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.posting.content[:10]}: {self.content[:20]}'

