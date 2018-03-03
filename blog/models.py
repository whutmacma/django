#coding:utf-8
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import markdown
from django.utils.html import strip_tags

# Create your models here.
class Category(models.Model):
    '''
    Category　用于存放文章的分类 Article的外键
    name  用于存放分类名
    '''
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    Tag 用于存放文章的标签　Article的外键
　　　　name 用于存放标签名
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    '''
    Aritcle  用于存放文章相关数据
　　　　title  文章标题
　　　　body  文章内容
    created_time  文章首次创建时间
    modified_time 文章最后一次修改时间
    excerpt  文章摘要
    category  文章分类　表Category的主键
    tags  文章标签   表Tag的主键
    author 文章作者
    views 文章阅读量
    '''
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):        
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Article, self).save(*args, **kwargs)
        
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
        
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
