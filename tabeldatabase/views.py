from django.shortcuts import render, redirect

from .models import (
    DataBobot,
    DataKriteria,
    DataKuliner,
    JenisUsaha,
    KonversiPenilaian,
)

# Create your views here.


def dataJenisUsaha(request):
    data_jenis_usaha = getData(JenisUsaha)
    data_field_jenis_usaha = getField(JenisUsaha)
    # print(data_field_jenis_usaha)
    return render(
        request,
        "tabeldatabase/datajenisusaha.html",
        {
            "namaData": "Jenis Usaha",
            "id": "Id_Usaha",
            "namaDB": "jenisusaha",
            "isiData": data_jenis_usaha,
            "isiFields": data_field_jenis_usaha,
        },
    )


def dataKuliner(request):
    data_kuliner = getData(DataKuliner)
    data_field_kuliner = getField(DataKuliner)
    # print(data_field_kuliner)
    return render(
        request,
        "tabeldatabase/datakuliner.html",
        {
            "namaData": "Kuliner",
            "id": "Id_Kuliner",
            "namaDB": "datakuliner",
            "isiData": data_kuliner,
            "isiFields": data_field_kuliner,
        },
    )

def dataKriteria(request):
    data_kriteria = getData(DataKriteria)
    data_field_kriteria = getField(DataKriteria)
    # print(data_field_kriteria)
    return render(
        request,
        "tabeldatabase/datakriteria.html",
        {
            "namaData": "Kriteria",
            "id": "Kode_Kriteria",
            "namaDB": "datakriteria",
            "isiData": data_kriteria,
            "isiFields": data_field_kriteria,
        },
    )


def dataBobot(request):
    data_bobot = getData(DataBobot)
    data_field_bobot = getField(DataBobot)
    # print(data_field_bobot)
    return render(
        request,
        "tabeldatabase/databobot.html",
        {
            "namaData": "Bobot",
            "id": "Id_Bobot",
            "namaDB": "databobot",
            "isiData": data_bobot,
            "isiFields": data_field_bobot,
        },
    )


def dataKonversiPenilaian(request):
    data_konversi_penilaian = getData(KonversiPenilaian)
    data_field_konversi_penilaian = getField(KonversiPenilaian)
    # print(data_field_konversi_penilaian)
    return render(
        request,
        "tabeldatabase/datakonversipenilaian.html",
        {
            "namaData": "Konversi Penilaian",
            "id": "Id_Konversi",
            "namaDB": "konversipenilaian",
            "isiData": data_konversi_penilaian,
            "isiFields": data_field_konversi_penilaian,
        },
    )

def getField(model):
    data = model._meta.get_fields()
    data_field = [
        field.name.replace("_", " ").title().replace(" ", "_") for field in data
    ]
    return data_field


def getData(model):
    data_bobot = model.objects.all()
    return data_bobot
