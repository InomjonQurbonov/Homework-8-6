from django.db import models


class Regulations(models.Model):
    reg_number = models.IntegerField()
    reg_date = models.DateField(auto_now_add=True)
    reg_sign = models.CharField(max_length=50)
    reg_title = models.CharField(max_length=50)
    reg_file = models.FileField(upload_to='regulations/')

    def __str__(self):
        return self.reg_number

    class Meta:
        ordering = ['reg_number']
        db_table = 'regulations'
        verbose_name = 'Regulation'
        verbose_name_plural = 'Regulations'
