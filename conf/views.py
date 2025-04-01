from django.views.generic import CreateView
from snap.forms import SnapForm
from snap.models import Snap
from utils.mixins import SuccessMessageMixin


class HomeView(SuccessMessageMixin, CreateView):
    model = Snap
    form_class = SnapForm
    template_name = "home/home.html"
    success_url = "/"
    success_message = "Snap uploaded successfully"

    def form_valid(self, form):
        snap = form.save(commit=False)
        if self.request.user.is_authenticated:
            snap.user = self.request.user
        snap.save()
        self.success_url = snap.get_detail_url()
        return super().form_valid(form)


home_view = HomeView.as_view()
