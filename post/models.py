from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110, unique=True, editable=False)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank = False)
    facebook = models.URLField(max_length=100, blank=True)    
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})

    def get_create_url(self):
        return reverse('post_create', kwargs={'slug':self.slug})
    
    def get_update_url(self):
        return reverse('post_update', kwargs={'slug':self.slug})
    
    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug':self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug=slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug= self.get_unique_slug()
        return super(Post,self).save(*args, **kwargs)

    class Meta:
       ordering = ('-publishing_date', 'id')
    
