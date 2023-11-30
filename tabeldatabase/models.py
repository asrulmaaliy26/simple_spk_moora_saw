from django.db import models

class DataKriteria(models.Model):
    kode_kriteria = models.CharField(max_length=255, primary_key=True)
    nama_kriteria = models.CharField(max_length=255)
    nilai_kriteria = models.FloatField()
    tipe_kriteria = models.CharField(max_length=1, choices=[('B', 'B'), ('C', 'C')])

    def __str__(self):
        return self.nama_kriteria

class DataBobot(models.Model):
    id_bobot = models.AutoField(primary_key=True)
    kode_kriteria = models.ForeignKey(DataKriteria, on_delete=models.CASCADE)
    nama_bobot = models.CharField(max_length=255)
    nilai_bobot = models.FloatField()

    def __str__(self):
        return self.nama_bobot

class DataKuliner(models.Model):
    id_kuliner = models.AutoField(primary_key=True)
    nama_usaha = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_usaha

class JenisUsaha(models.Model):
    id_usaha = models.AutoField(primary_key=True)
    nama_jenis = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_jenis

class KonversiPenilaian(models.Model):
    id_konversi = models.AutoField(primary_key=True)
    nama_usaha = models.CharField(max_length=255, default='')
    C1 = models.IntegerField()
    C2 = models.IntegerField()
    C3 = models.IntegerField()
    C4 = models.IntegerField()
    C5 = models.IntegerField()

    def __str__(self):
        return self.nama_usaha
