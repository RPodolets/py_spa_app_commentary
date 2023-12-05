from django.urls import path

# from core.views import CommentaryListView
from core.views import commentary_list

app_name = "core"

urlpatterns = [
    path("", commentary_list, name="commentary-list")
]