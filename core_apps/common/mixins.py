from django.contrib.auth.mixins import LoginRequiredMixin


class SetUserMixin(LoginRequiredMixin):
    user_field = "created_by"

    def form_valid(self, form):
        setattr(form.instance, self.user_field, self.request.user)
        return super().form_valid(form)
