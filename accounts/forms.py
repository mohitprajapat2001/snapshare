from django.forms import (
    ModelForm,
    Form,
    CharField,
    TextInput,
    PasswordInput,
    ValidationError,
)
from utils.constants import FormValdationMessages
from django.contrib.auth import get_user_model
from accounts.constants import FormCostants, INPUT_CLASS
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserRegistrationForm(ModelForm):
    confirm_password = CharField(
        required=True,
        widget=PasswordInput(attrs={"class": INPUT_CLASS}),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password", "confirm_password")
        widgets = {}
        labels = {}
        for field in fields:
            input_type = TextInput
            input_class = INPUT_CLASS
            if field in ["password", "confirm_password"]:
                input_type = PasswordInput
            widgets[field] = input_type(attrs={"class": input_class})
            labels[field] = FormCostants.lABELS[field]

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise ValidationError(FormValdationMessages.EMPTY_FIELD)
        return first_name

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise ValidationError(FormValdationMessages.EMPTY_FIELD)
        validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError(
                {"confirm_password": FormValdationMessages.PASSWORD_MISMATCH}
            )
        password = self.cleaned_data.get("password")
        return cleaned_data


class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        widgets = {}
        labels = {}
        for field in fields:
            input_type = TextInput
            input_class = INPUT_CLASS
            widgets[field] = input_type(attrs={"class": input_class})
            labels[field] = FormCostants.lABELS[field]


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={"class": INPUT_CLASS}))
    password = CharField(widget=PasswordInput(attrs={"class": INPUT_CLASS}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            self.user = None
        return cleaned_data
