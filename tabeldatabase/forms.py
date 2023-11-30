from django.forms import ModelForm

from .models import DataBobot, DataKriteria, DataKuliner, KonversiPenilaian


class DataBobotForm(forms.ModelForm):
    class Meta:
        model = DataBobot
        fields = "__all__"

class DataKriteriaForm(forms.ModelForm):
    class Meta:
        model = DataKriteria
        fields = "__all__"


class DataKulinerForm(forms.ModelForm):
    class Meta:
        model = DataKuliner
        fields = "__all__"


class Jenis_UsahaForm(forms.ModelForm):
    class Meta:
        model = Jenis_Usaha
        fields = "__all__"


class KonversiPenilaianForm(forms.ModelForm):
    class Meta:
        model = KonversiPenilaian
        fields = "__all__"
