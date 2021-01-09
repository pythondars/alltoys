from django import forms

from toys.models import Toy


class ToyAdminForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop("initial", None)
        instance = kwargs.pop("instance", None)

        super(ToyAdminForm, self).__init__(*args, **kwargs)
