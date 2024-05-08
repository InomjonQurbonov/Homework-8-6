from django.db import models


class Standards(models.Model):
    standard_title = models.CharField(max_length=100)
    standard_number = models.CharField(max_length=100)
    standard_date = models.IntegerField()  # faqat yilni kiritish uchun
    standard_name = models.CharField(max_length=100)
    standard_file = models.FileField(upload_to='standards/')

    def __str__(self):
        return self.standard_name

    class Meta:
        db_table = 'standards'
        verbose_name = 'Standard'
        verbose_name_plural = 'Standards'
