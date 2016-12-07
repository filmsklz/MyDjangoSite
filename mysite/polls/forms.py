# -*- coding: utf-8 -*-
from django import forms

from .models import Cpudata


class CpudataForm(forms.ModelForm):

    class Meta:
        model = Cpudata
        fields = ('brand', 'gen', 'insurance', 'years', 'price')


class CpudataForm2(forms.ModelForm):

    class Meta:
        model = Cpudata
        fields = ('brand', 'gen', 'insurance', 'years')