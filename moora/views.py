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
from .moora import getNormalisasi, getWeightNormalisasi, getNilaiRanking, getWeightedNormalizedData

def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "index.html")

def penilaian(request):
    weighted_normalized_data = getWeightedNormalizedData()
    return render(request, "moora/penilaian.html",  {'weighted_normalized_data': weighted_normalized_data})

def normalisasi(request):
    context = {
        "normalized_data": getNormalisasi(),
    }
    # print(context)
    return render(request, "moora/normalisasi.html", context)

def perangkingan(request):
    ranking_results = getNilaiRanking()
    
    context = {'ranking_results': ranking_results}
    return render(request, 'moora/perangkingan.html', context)

def keputusan(request):
    ranking_results = getNilaiRanking()
    
    context = {'ranking_results': ranking_results}
    return render(request, "moora/keputusan.html", context)
