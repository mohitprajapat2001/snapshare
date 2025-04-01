from django.contrib.messages import info


class SuccessMessageMixin:
    success_message = None

    def get_success_url(self, *args, **kwargs):
        if self.success_message:
            info(self.request, self.success_message)
        return super().get_success_url(*args, **kwargs)
