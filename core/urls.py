from django.urls import path

from core.views import commentary_list, reply_view

app_name = "core"

urlpatterns = [
    path("", commentary_list, name="commentary-list"),
    path("reply/", reply_view, name="reply"),
]
