from django.db import models

# Create your models here.

class Paket(models.Model):
    naziv = models.CharField(max_length=40)
    cijena = models.FloatField()

    def __str__(self):
        return self.naziv

class Korisnik(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=40)
    datum_rodenja = models.DateField('date of birth')
    opcija_paket = models.ForeignKey(Paket, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ime)
