from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^(\+20|0)1[0125]\d{8}$',
    message='Enter a valid Egyptian mobile number, e.g. 01012345678.',
)

class Category(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('won', 'Won'),
      ('lost', 'Lost'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='records')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT )
    phone = models.CharField(max_length=20, validators=[phone_validator])
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

    class Meta:
        ordering = ['-created_at']
