from django.urls import path, re_path
from . import views

app_name = "signage"

urlpatterns = [
    path("displays/", views.DisplayList.as_view(), name="display_list"),
    path("display/create/", views.DisplayCreate.as_view(), name="display_create"),
    path(
        "display/<int:pk>/delete/", views.DisplayDelete.as_view(), name="display_delete"
    ),
    path(
        "display/<int:pk>/update/", views.DisplayUpdate.as_view(), name="display_update"
    ),
    path("display/<int:pk>/", views.DisplayDetail.as_view(), name="display_view"),
    path("slides/", views.SlideList.as_view(), name="slide_list"),
    path("slide/create/", views.SlideCreate.as_view(), name="slide_create"),
    path("slide/<int:pk>/delete/", views.SlideDelete.as_view(), name="slide_delete"),
    path("slide/<int:pk>/update/", views.SlideUpdate.as_view(), name="slide_update"),
    path("videos/", views.VideoList.as_view(), name="video_list"),
    path("video/create/", views.VideoCreate.as_view(), name="video_create"),
    path("video/<int:pk>/delete/", views.VideoDelete.as_view(), name="video_delete"),
    path("video/<int:pk>/update/", views.VideoUpdate.as_view(), name="video_update"),
]
