from django.contrib import admin
from .models import DataBobot, DataKriteria, DataKuliner, JenisUsaha, KonversiPenilaian

# Register your models here.
admin.site.register(DataBobot)
admin.site.register(DataKriteria)
admin.site.register(DataKuliner)
admin.site.register(JenisUsaha)
admin.site.register(KonversiPenilaian)