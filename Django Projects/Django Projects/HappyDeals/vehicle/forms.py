from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'vehicle_type', 'max_persons', 'fuel_efficiency', 'price_per_km', 'availability', 'image_url']
