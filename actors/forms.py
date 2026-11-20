from django import forms
from actors.models import Actors


class ActorForm(forms.ModelForm):
    class Meta:
        model=Actors
        fields = ["name", "place", "about", "dob", "picture"]
        labels = {
            "name": "Actor name",
            "place": "Place",
            "about": "About",
            "dob": "Date of birth",
            "picture": "Photo",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter actor name",
            }),
            "place": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter actor's place",
            }),
            "about": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write a short biography",
                "rows": 5,
            }),
            "dob": forms.DateInput(
                attrs={"class": "form-control", "type": "date"},
                format="%Y-%m-%d",
            ),
            "picture": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
            }),
        }