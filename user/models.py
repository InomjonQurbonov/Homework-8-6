from django.contrib.auth import get_user_model
from django.db import models
from app_leadership.models import Leadership


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'


class Contacts(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    message_file = models.FileField(upload_to='messages')
    for_leadership = models.ForeignKey(Leadership, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
