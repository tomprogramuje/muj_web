from django.db import models

# Create your models here.


class Vzdelani(models.Model):
    instituce = models.CharField(max_length=250)
    titul = models.CharField(max_length=100)
    doba = models.CharField(max_length=150)
    obor = models.CharField(max_length=100)
    popis = models.CharField(max_length=500)

    def __str__(self):
        return "{} {} {} {} {}".format(self.instituce, self.titul, self.doba, self.obor, self.popis)

    class Meta:
        verbose_name = "Vzdělání"
        verbose_name_plural = "Vzdělání"


class PracovniZkusenost(models.Model):
    pozice = models.CharField(max_length=100)
    zamestnavatel = models.CharField(max_length=100)
    doba = models.CharField(max_length=150)
    napln = models.CharField(max_length=500)

    def __str__(self):
        return "{} {} {} {}".format(self.pozice, self.zamestnavatel, self.doba, self.napln)

    class Meta:
        verbose_name = "Pracovní zkušenost"
        verbose_name_plural = "Pracovní zkušenosti"


class Projekt(models.Model):
    nazev = models.CharField(max_length=150)
    urceni = models.CharField(max_length=150)
    doba = models.CharField(max_length=150)
    detail = models.CharField(max_length=500)

    def __str__(self):
        return "{} {} {}".format(self.nazev, self.urceni, self.doba, self.detail)

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"
