from django import forms
from .models import Drone

class DroneForm(forms.ModelForm):  # forms.Form o'rniga forms.ModelForm dan foydalanamiz
    class Meta:
        model = Drone
        fields = ['id', 'brand', 'name']  # Saqlamoqchi bo'lgan model maydonlarini kiritamiz
