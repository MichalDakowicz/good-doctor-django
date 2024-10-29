from django.db import models

# Create your models here.
class Pacjent(models.Model):
    nazwisko = models.CharField(max_length=50)
    imie = models.CharField(max_length=50)
    miasto = models.CharField(max_length=50, default="Białystok")
    ulica = models.CharField(max_length=50)
    wiek = models.IntegerField()
    
    def __str__(self):
        return self.nazwisko + ' ' + self.imie

class Wizyta(models.Model):
    data = models.DateField()
    zlecenia = models.TextField()
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pacjent.nazwisko + ' ' + self.pacjent.imie + ' ' + str(self.data)
