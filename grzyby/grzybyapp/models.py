from django.db import models

class Rodzina(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Potrawa(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Grzyby(models.Model):
    nazwa = models.CharField(max_length=100)
    potoczna = models.CharField(max_length=100)
    jadalny = models.CharField(max_length=100)
    miesiac_zbierania = models.TextField()
    rodzina = models.ForeignKey(Rodzina, on_delete=models.CASCADE)
    potrawa = models.ForeignKey(Potrawa, on_delete=models.CASCADE)
    def __str__(self):
        return f" {self.nazwa} nazwa potoczna: {self.potoczna} należy do rodziny: {self.rodzina}"