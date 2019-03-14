from django.contrib import admin
from .models import Posting

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 개발화면에서 확인만 가능
    list_display = ('id', 'content', 'created_at', 'updated_at') # 리스트에서 보여질 컬럼들
    list_display_links = ('id', 'content') # 리스트에서 clickable columns

# Register your models here.
admin.site.register(Posting, PostingModelAdmin)
