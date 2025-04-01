from django.contrib.messages import info


class SuccessMessageMixin:

    def get_success_url(self, *args, **kwargs):
        info(self.request, self.success_message)
        return super().get_success_url(*args, **kwargs)
