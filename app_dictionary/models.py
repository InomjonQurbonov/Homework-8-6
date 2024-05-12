from django.db import models


class Dictionary(models.Model):
    dict_number = models.IntegerField(unique=True)
    word_uzb = models.CharField(max_length=100)
    word_rus = models.CharField(max_length=100)
    word_eng = models.CharField(max_length=100)
    word_turk = models.CharField(max_length=100)
    word_meaning = models.TextField(blank=True)

    def __str__(self):
        return self.word_uzb

    class Meta:
        db_table = 'dictionary'
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'
