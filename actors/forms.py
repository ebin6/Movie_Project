from django import forms
from actors.models import Actors


class ActorForm(forms.ModelForm):
    class Meta:
        model=Actors
        fields="__all__"