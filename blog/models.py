from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='tagName')

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


    def __str__(self):
        return self.name

# article category
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='categoryName')
    index = models.IntegerField(verbose_name='categoryPriority', default=999)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name

# article
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='articleTitle')
    desc = models.CharField(max_length=50, verbose_name='articleDescription')
    content = models.TextField(verbose_name='articleContent')
    click_count = models.IntegerField(default=0, verbose_name='clickTimes')
    is_recommend = models.BooleanField(default=False, verbose_name='isRecommend')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='publishDate')
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

# user comment
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章', on_delete=models.CASCADE)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return str(self.id)

# blogroll
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序（从小到大）')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title


# advertise
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    description = models.CharField(max_length=200, verbose_name='图片路径')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title