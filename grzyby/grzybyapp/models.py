from django.db import models

class Rodzina(models.Model):
    nazwa = models.TextField()
    def __str__(self):
        return self.nazwa

class Potrawa(models.Model):
    nazwa = models.TextField()
    def __str__(self):
        return self.nazwa

class Grzyby(models.Model):
    nazwa = models.TextField()
    potoczna = models.TextField()
    jadalny = models.TextField()
    miesiac_zbierania = models.TextField()
    rodzina = models.ForeignKey(Rodzina, on_delete=models.CASCADE)
    potrawa = models.ForeignKey(Potrawa, on_delete=models.CASCADE)