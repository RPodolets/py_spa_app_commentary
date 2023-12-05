from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from core.forms import CommentaryForm
from core.models import Commentary, User


def commentary_list(request: HttpRequest) -> HttpResponse:
    commentaries = Commentary.objects.filter(parent=None)
    form = CommentaryForm()

    if request.method == "POST":
        comment_form = CommentaryForm(data=request.POST)
        if comment_form.is_valid():
            results = comment_form.cleaned_data
            user = User.objects.create(
                username=results["username"],
                email=results["email"],
                home_page=results["home_url"]
            )
            Commentary.objects.create(
                user=user,
                body=results["text"]
            )

    return render(
        request,
        "core/commentary_list.html",
        context={
            "commentary_list": commentaries,
            "form": form
        }
    )


def reply_view(request):
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        parent_id = request.POST.get("parent")

        if form.is_valid():
            results = form.cleaned_data
            print(results, parent_id)
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

    return redirect("/")
