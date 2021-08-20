from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20, unique=True)
    nativeName = models.CharField(max_length=20)
    iso639_1 = models.CharField(max_length=10)
    iso639_2 = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Timezone(models.Model):
    name = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Border(models.Model):
    name = models.CharField(max_length=5, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    alphacode2 = models.CharField(max_length=10)
    alphacode3 = models.CharField(max_length=10)
    capital = models.CharField(max_length=30)
    population = models.PositiveIntegerField()
    timezone = models.ManyToManyField(Timezone)
    flag = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)
    neighbouring = models.ManyToManyField(Border, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
