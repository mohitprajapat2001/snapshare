from django.views.generic import FormView, View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.messages import info
from django.shortcuts import redirect
from utils.constants import Templates, FormSuccessMessages, FormValdationMessages
from django.urls import reverse_lazy
from accounts.forms import UserRegistrationForm, LoginForm, UserProfileUpdateForm
from utils.mixins import SuccessMessageMixin

User = get_user_model()


class BaseAccountsView:

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            info(request, FormSuccessMessages.USER_ALREADY_LOGGED_IN)
            return redirect(reverse_lazy("home"))
        return super(BaseAccountsView, self).get(request, *args, **kwargs)


class RegisterView(BaseAccountsView, SuccessMessageMixin, FormView):
    template_name = Templates.REGISTER_TEMPLATE
    form_class = UserRegistrationForm
    success_url = "/accounts/login/"
    success_message = FormSuccessMessages.USER_REGISTERED

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)


register_view = RegisterView.as_view()


class LoginView(BaseAccountsView, SuccessMessageMixin, FormView):
    template_name = Templates.LOGIN_TEMPLATE
    form_class = LoginForm
    success_url = "/"
    success_message = FormSuccessMessages.USER_LOGIN

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if not user:
            form.add_error(None, FormValdationMessages.USER_NOT_FOUND)
            return super().form_invalid(form)
        if not user.is_active:
            form.add_error(None, FormValdationMessages.USER_NOT_ACTIVE)
            return super().form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)


login_view = LoginView.as_view()


class LogoutView(View):
    def get(self, request):
        logout(request)
        info(request, FormSuccessMessages.USER_LOGOUT)
        return redirect(reverse_lazy("home"))


logout_view = LogoutView.as_view()


class ProfileView(SuccessMessageMixin, FormView):
    model = User
    template_name = Templates.PROFILE_TEMPLATE
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy("accounts:profile")
    success_message = FormSuccessMessages.USER_UPDATED

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            info(request, FormSuccessMessages.USER_NOT_LOGGED_IN)
            return redirect(reverse_lazy("home"))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


profile_view = ProfileView.as_view()
