import math
from django.db import models
from tabeldatabase.models import KonversiPenilaian, DataKriteria

def getNormalisasi():
    try:
        konversi_data = KonversiPenilaian.objects.all()

        n1_squared = 0
        n2_squared = 0
        n3_squared = 0
        n4_squared = 0
        n5_squared = 0
        
        c1_values = [] 
        c2_values = [] 
        c3_values = [] 
        c4_values = [] 
        c5_values = [] 

        normalized_data = []  # Create a list to store the normalized data
        for item in konversi_data:
            n1_squared += item.C1**2
            n2_squared += item.C2**2
            n3_squared += item.C3**2
            n4_squared += item.C4**2
            n5_squared += item.C5**2
            
            c1_values.append(item.C1)
            c2_values.append(item.C2)
            c3_values.append(item.C3)
            c4_values.append(item.C4)
            c5_values.append(item.C5)
            
        for item in konversi_data:
            n1_normalized = item.C1 / math.sqrt(n1_squared)
            n2_normalized = item.C2 / math.sqrt(n2_squared)
            n3_normalized = item.C3 / math.sqrt(n3_squared)
            n4_normalized = item.C4 / math.sqrt(n4_squared)
            n5_normalized = item.C5 / math.sqrt(n5_squared)

            normalized_data.append({
                'nama_usaha': item.nama_usaha,
                'C1': item.C1,
                'C2': item.C2,
                'C3': item.C3,
                'C4': item.C4,
                'C5': item.C5,
                'C1v' : c1_values,
                'C2v' : c2_values,
                'C3v' : c3_values,
                'C4v' : c4_values,
                'C5v' : c5_values,
                'n1_normalized': round(n1_normalized, 3),
                'n2_normalized': round(n2_normalized, 3),
                'n3_normalized': round(n3_normalized, 3),
                'n4_normalized': round(n4_normalized, 3),
                'n5_normalized': round(n5_normalized, 3),
            })
    except Exception as e:
        print(f"Error in getNormalisasi: {str(e)}")
        normalized_data = []
        
    return normalized_data

def getWeightNormalisasi():
    try:
        weights = DataKriteria.objects.values('nilai_kriteria')
        weight_data = []

        for weight in weights:
            weight_data.append({
                'nilai_bobot': weight['nilai_kriteria'],
            })
    except Exception as e:
        print(f"Error in getWeightNormalisasi: {str(e)}")
        weight_data = []

    return weight_data

def getWeightedNormalizedData():
    normalized_data = getNormalisasi()
    weight_data = getWeightNormalisasi()

    results = []

    for data in normalized_data:
        weighted_data = {
            'nama_usaha': data['nama_usaha'],
            'n1_weighted': float(data['n1_normalized']) * float(weight_data[0]['nilai_bobot']),
            'n2_weighted': float(data['n2_normalized']) * float(weight_data[1]['nilai_bobot']),
            'n3_weighted': float(data['n3_normalized']) * float(weight_data[2]['nilai_bobot']),
            'n4_weighted': float(data['n4_normalized']) * float(weight_data[3]['nilai_bobot']),
            'n5_weighted': float(data['n5_normalized']) * float(weight_data[4]['nilai_bobot']),
            'bobot1': weight_data[0]['nilai_bobot'],
            'bobot2': weight_data[1]['nilai_bobot'],
            'bobot3': weight_data[2]['nilai_bobot'],
            'bobot4': weight_data[3]['nilai_bobot'],
            'bobot5': weight_data[4]['nilai_bobot'],
            'n1_normalized': data['n1_normalized'],
            'n2_normalized': data['n2_normalized'],
            'n3_normalized': data['n3_normalized'],
            'n4_normalized': data['n4_normalized'],
            'n5_normalized': data['n5_normalized'],
        }
        results.append(weighted_data)
    # print(results)
    return results

def getNilaiRanking():
    get_Weighted_Normalized_Data = getWeightedNormalizedData();
    try:
        ranking_results = []

        for item in get_Weighted_Normalized_Data:
            ranking_value = (round(item['n1_weighted'],3) + item['n2_weighted'] + round(item['n4_weighted'],3)) - (item['n3_weighted'] + item['n5_weighted'])

            ranking_results.append({
                'nama_usaha': item['nama_usaha'],
                'ranking_value': ranking_value,
                'n1_weighted': item['n1_weighted'],
                'n2_weighted': item['n2_weighted'],
                'n3_weighted': item['n3_weighted'],
                'n4_weighted': item['n4_weighted'],
                'n5_weighted': item['n5_weighted'],
            })

    except Exception as e:
        print(f"Error in calculateRanking: {str(e)}")
        ranking_results = []

    return ranking_results