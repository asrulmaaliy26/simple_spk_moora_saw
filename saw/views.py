from django.shortcuts import render
from django.db import models
from decimal import Decimal
from django.db.models import Max, Min
from tabeldatabase.models import (
    DataBobot,
    DataKriteria,
    DataKuliner,
    JenisUsaha,
    KonversiPenilaian,
)
from .saw import getNormalisasi, getWeightNormalisasi, getNilaiRanking

def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "index.html")

def penilaian(request):
    nama_usaha_list = DataKuliner.objects.values_list("nama_usaha", flat=True)
    return render(request, "saw/penilaian.html")

def normalisasi(request):
    maxmin_data = KonversiPenilaian.objects.aggregate(
        maxminK1=models.Max("C1"), maxminK2=models.Max("C2"), maxminK3=models.Min("C3"), maxminK4=models.Max("C4"), maxminK5=models.Min("C5")
    )

    context = {
        "maxmin": maxmin_data,
        "normalized_data": getNormalisasi(),
    }
    return render(request, "saw/normalisasi.html", context)

def perangkingan(request):
    context = {"ranked_results": getNilaiRanking()}

    return render(request, "saw/perangkingan.html", context)

def keputusan(request):
    ranking_results = getNilaiRanking()
    threshold = 0.8

    for result in ranking_results:
        result["status"] = (
            "Mendapat" if result["total_weighted"] > threshold else "Tidak Mendapat Bantuan"
        )

    context = {"ranked_results": ranking_results}
    return render(request, "saw/keputusan.html", context)
