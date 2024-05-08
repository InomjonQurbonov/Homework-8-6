from django.db import models


class Leadership(models.Model):
    leader_full_name = models.CharField(max_length=100)
    leader_position = models.CharField(max_length=100)
    leader_email = models.CharField(max_length=100)
    leader_phone_number = models.CharField(max_length=100)
    leader_Works_days = models.CharField(max_length=100)
    leader_spessionality = models.CharField(max_length=500)

    def __str__(self):
        return self.leader_full_name

    class Meta:
        db_table = 'leadership'
        verbose_name = 'Leadership'


class StructuralUnits(models.Model):
    department_name = models.CharField(max_length=200)
    boss_full_name = models.CharField(max_length=100)
    boss_email = models.CharField(max_length=100)
    boss_phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'structural_units'
        verbose_name = 'Structural Units'
        verbose_name_plural = 'Structural Units'
