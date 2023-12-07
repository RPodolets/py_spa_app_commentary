from django.shortcuts import redirect
from django.views.generic import ListView

from core.forms import CommentaryForm
from core.models import Commentary, User

ITEMS_PER_PAGE = 25


class CommentaryListView(ListView):
    model = Commentary
    paginate_by = ITEMS_PER_PAGE

    def get_queryset(self):
        queryset = Commentary.objects.filter(parent=None)
        sort_param = self.request.GET.get("sort")
        order_param = self.request.GET.get("order")

        if order_param == "desc":
            sort_param = f"-{sort_param}"

        if sort_param in ("created", "email", "username"):
            if sort_param == "created":
                return queryset.order_by(sort_param)
            return queryset.order_by(f"user__{sort_param}")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentaryForm()
        order_param = self.request.GET.get("order")
        print(order_param)
        context["order_param"] = (
            "asc" if order_param == "desc" else "desc"
        )
        return context

    def post(self, request, *args, **kwargs):
        form_valid_create_obj(self.request)
        return self.get(request, *args, **kwargs)


def form_valid_create_obj(request):
    form = CommentaryForm(data=request.POST)
    parent_id = request.POST.get("parent")

    if form.is_valid():
        results = form.cleaned_data
        user = User.objects.create(
            username=results["username"],
            email=results["email"],
            home_page=results["home_url"]
        )
        Commentary.objects.create(
            user=user,
            parent_id=parent_id,
            body=results["text"]
        )


def reply_view(request):
    if request.method == "POST":
        form_valid_create_obj(request)

    return redirect("/")
