from django.contrib.admin import register, ModelAdmin
from admin_auto_filters.filters import AutocompleteFilter
from snap.models import Snap


class UserFilter(AutocompleteFilter):
    title = "User"
    field_name = "user"


@register(Snap)
class SnapAdmin(ModelAdmin):
    readonly_fields = ("snap",)
    list_filter = (UserFilter,)
