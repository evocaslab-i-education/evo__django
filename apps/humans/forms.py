from django import forms

from apps.humans.models import Human


class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ('name', 'age',)
