from django.http import HttpResponse
from django.views import View, generic
from snap.models import Snap
from accounts.models import User


class SnapView(View):

    def get(self, request, *args, **kwargs):
        try:
            snap = Snap.objects.get(**kwargs)
            return HttpResponse(snap.image.read(), content_type="image/png")
        except Snap.DoesNotExist:
            return HttpResponse("Snap not found", status=404)


snap_view = SnapView.as_view()


class SnapDetail(generic.DetailView):
    model = Snap
    context_object_name = "snap"
    slug_field = "snap"
    slug_url_kwarg = "snap"
    template_name = "snap/detail.html"


snap_detail = SnapDetail.as_view()


class SnapList(generic.TemplateView):
    template_name = "snap/list.html"


snap_list = SnapList.as_view()
