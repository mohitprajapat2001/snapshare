from django.utils.translation import gettext_lazy as _

INPUT_CLASS = "input w-full"


class FormCostants:
    lABELS = {
        "username": _("Username"),
        "password": _("Password"),
        "first_name": _("First Name"),
        "last_name": _("Last Name"),
        "email": _("Email"),
        "confirm_password": _("Confirm Password"),
    }
    PLACEHOLDERS = (
        {
            "username": _("Enter Username"),
            "password": _("Enter Password"),
            "first_name": _("Enter First Name"),
            "last_name": _("Enter Last Name"),
            "email": _("Enter Email"),
            "confirm_password": _("Confirm Password"),
        },
    )
