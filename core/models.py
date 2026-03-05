from django.db import models
from phonenumber_field.modelfields  import PhoneNumberField

class Organization(models.Model):
    name            = models.CharField(max_length=255)
    contact_name    = models.CharField(max_length=255)
    contact_email   = models.EmailField()
    contact_phone   = PhoneNumberField()
    description     = models.TextField(blank=True, null=True)
    url             = models.URLField(blank=True, null=True)
    slug            = models.SlugField(unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.name

class Program(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField(blank=True, null=True)
    organization    = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='programs')
    url             = models.URLField(blank=True, null=True)
    slug            = models.SlugField(unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.name