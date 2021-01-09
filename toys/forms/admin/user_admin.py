from django import forms

from toys.models import User


class UserAdminForm(forms.ModelForm):
    email = forms.EmailField(label="User email", required=True)

    class Meta:
        model = User
        fields = "__all__"
