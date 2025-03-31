from django.forms import ModelForm, FileInput
from snap.models import Snap
from snap.constants import FILE_INPUT_CLASS


class SnapForm(ModelForm):

    class Meta:
        model = Snap
        fields = ("image",)
        widgets = {
            "image": FileInput(
                attrs={
                    "accept": "image/*",
                    "class": FILE_INPUT_CLASS,
                }
            )
        }
