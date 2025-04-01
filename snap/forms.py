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

    def clean(self):
        """
        check for image size and accept format allow png,jpg,jpeg formats
        """
        cleaned_data = super().clean()
        image = cleaned_data.get("image")
        if image:
            if image.size > 1024 * 1024 * 2:
                self.add_error("image", "Image size should be less than 2MB")
            if image.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
                self.add_error("image", "Image format should be png,jpg,jpeg")
        return cleaned_data
