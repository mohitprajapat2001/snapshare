from django.views.generic import CreateView
from snap.forms import SnapForm
from snap.models import Snap


class HomeView(CreateView):
    model = Snap
    form_class = SnapForm
    template_name = "home/home.html"
    success_url = "/"

    def form_valid(self, form):
        breakpoint()
        return super().form_valid(form)


home_view = HomeView.as_view()
