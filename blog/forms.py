from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica classes padrão a todos os campos
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control"
            })

    def is_valid(self):
        valid = super().is_valid()
        # Adiciona classe "is-invalid" nos campos com erro
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                existing_classes = field.widget.attrs.get("class", "")
                field.widget.attrs["class"] = f"{existing_classes} is-invalid"
        return valid