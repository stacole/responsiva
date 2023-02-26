from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from django import forms
from .models import Resguardos

JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

class ResguardosForm(forms.ModelForm):
    class Meta:
        model = Resguardos
        fields = ["name", "gid", "department", "position", "device","detail", "signature"]

