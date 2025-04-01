from django.urls import path
from snap.views import snap_view, snap_detail, snap_list


app_name = "snap"

urlpatterns = [
    path("<str:snap>/", snap_view, name="view"),
    path("list/", snap_list, name="list"),
    path("view/<str:snap>/", snap_detail, name="detail"),
]
