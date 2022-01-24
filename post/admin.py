from django.contrib import admin
from . models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'publishing_date')
    list_filter = ('publishing_date',)
    search_fields = ('title', 'content')

    class Meta:
        model = Post

