from django.db import models
from tabeldatabase.models import KonversiPenilaian, DataKriteria


def getNormalisasi():
    try:
        maxmin_data = KonversiPenilaian.objects.aggregate(
            maxK1=models.Max('C1'),
            maxK2=models.Max('C2'),
            minK3=models.Min('C3'),
            maxK4=models.Max('C4'),
            minK5=models.Min('C5')
        )
        print(maxmin_data)
        konversi_data = KonversiPenilaian.objects.all()

        normalized_data = []  # Create a list to store the normalized data
        for item in konversi_data:
            n1_normalized = float(item.C1) / float(maxmin_data['maxK1'])
            n2_normalized = float(item.C2) / float(maxmin_data['maxK2'])
            n3_normalized = float(maxmin_data['minK3']) / float(item.C3)
            n4_normalized = float(item.C4) / float(maxmin_data['maxK4'])
            n5_normalized = float(maxmin_data['minK5']) / float(item.C5)
            # print(item.C1)

            normalized_data.append({
                'nama_usaha': item.nama_usaha,
                'C1': item.C1,
                'C2': item.C2,
                'C3': item.C3,
                'C4': item.C4,
                'C5': item.C5,
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
                'nilai_bobot': float(weight['nilai_kriteria']),
            })
    except Exception as e:
        print(f"Error in getWeightNormalisasi: {str(e)}")
        weight_data = []

    return weight_data

def getNilaiRanking():
    try:
        normalized_data = getNormalisasi()
        weight_data = getWeightNormalisasi()

        results = []

        for data in normalized_data:
            n1_normalized = data['n1_normalized']
            n2_normalized = data['n2_normalized']
            n3_normalized = data['n3_normalized']
            n4_normalized = data['n4_normalized']
            n5_normalized = data['n5_normalized']

            n1_weighted = n1_normalized * weight_data[0]['nilai_bobot']
            n2_weighted = n2_normalized * weight_data[1]['nilai_bobot']
            n3_weighted = n3_normalized * weight_data[2]['nilai_bobot']
            n4_weighted = n4_normalized * weight_data[3]['nilai_bobot']
            n5_weighted = n5_normalized * weight_data[4]['nilai_bobot']
            
            # print(weight_data[1]['nilai_bobot'])
            # print(n2_weighted)

            total_weighted = n1_weighted + n2_weighted + n3_weighted + n4_weighted + n5_weighted
            results.append({
                'nama_usaha': data['nama_usaha'],
                'n1_normalized': n1_normalized,
                'n2_normalized': n2_normalized,
                'n3_normalized': n3_normalized,
                'n4_normalized': n4_normalized,
                'n5_normalized': n5_normalized,
                'nilai_bobot1': weight_data[0]['nilai_bobot'],
                'nilai_bobot2': weight_data[1]['nilai_bobot'],
                'nilai_bobot3': weight_data[2]['nilai_bobot'],
                'nilai_bobot4': weight_data[3]['nilai_bobot'],
                'nilai_bobot5': weight_data[4]['nilai_bobot'],
                'n1_weighted': n1_weighted,
                'n2_weighted': n2_weighted,
                'n3_weighted': n3_weighted,
                'n4_weighted': n4_weighted,
                'n5_weighted': n5_weighted,
                'total_weighted': total_weighted,
            })
    except Exception as e:
        print(f"Error in getNilaiRanking: {str(e)}")
        results = []

    return results


