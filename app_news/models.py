from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_description = models.CharField(max_length=200)
    news_image = models.ImageField(upload_to='news/%Y/%m/%d/')
    news_content = models.TextField()
    news_date = models.DateField(auto_now_add=True)
    news_views = models.IntegerField(default=0)
    news_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_title

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['news_date']


class Announcement(models.Model):
    anno_title = models.CharField(max_length=200)
    anno_description = models.CharField(max_length=200)
    anno_image = models.ImageField(upload_to='anno/%Y/%m/%d/')
    anno_date = models.DateField(auto_now_add=True)
    anno_content = models.TextField()
    anno_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.anno_title

    class Meta:
        db_table = 'anno'
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'
        ordering = ['anno_date']
