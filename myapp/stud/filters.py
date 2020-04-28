import django_filters

from .models import Computer
from django import forms
class studFilter(django_filters.FilterSet):
    class Meta:
        model = Computer
        fields = ['degree', 'dept', 'year']
        widgets = {
            'degree': forms.Select(attrs={
                'class': 'form-control',

            }),
            'dept': forms.Select(attrs={
                'class': 'form-control',
            }),
            'year': forms.Select(attrs={
                'class': 'form-control',
            }),
        }   