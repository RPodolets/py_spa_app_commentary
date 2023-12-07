from django.urls import path

from core.views import reply_view, CommentaryListView

app_name = "core"

urlpatterns = [
    path("", CommentaryListView.as_view(), name="commentary-list"),
    path("reply/", reply_view, name="reply"),
]
