from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    surname_at_birth = models.CharField(max_length=100, null=True, blank=True)
    birth_day = models.IntegerField(null=True, blank=True)
    birth_month = models.IntegerField(null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    death_day = models.IntegerField(null=True, blank=True)
    death_month = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    place_of_death = models.CharField(max_length=100, null=True, blank=True)
    is_living = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')), null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
