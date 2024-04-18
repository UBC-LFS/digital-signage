from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Display, Slide, Video


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class DisplayDetail(DetailView):
    model = Display


class DisplayList(StaffRequiredMixin, ListView):
    model = Display


class DisplayCreate(StaffRequiredMixin, CreateView):
    model = Display
    fields = ["name", "update_interval", "tags"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DisplayDelete(StaffRequiredMixin, DeleteView):
    model = Display
    success_url = reverse_lazy("signage:display_list")


class DisplayUpdate(StaffRequiredMixin, UpdateView):
    model = Display
    fields = ["name", "update_interval", "tags"]


class SlideList(StaffRequiredMixin, ListView):
    model = Slide


class SlideCreate(StaffRequiredMixin, CreateView):
    model = Slide
    fields = [
        "name",
        "image",
        "start",
        "end",
        # "duration",
        "weight",
        "tags",
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class SlideDelete(StaffRequiredMixin, DeleteView):
    model = Slide
    success_url = reverse_lazy("signage:slide_list")


class SlideUpdate(StaffRequiredMixin, UpdateView):
    model = Slide
    fields = [
        "name",
        "image",
        "start",
        "end",
        # "duration",
        "weight",
        "tags",
    ]


class VideoList(StaffRequiredMixin, ListView):
    model = Video


class VideoCreate(StaffRequiredMixin, CreateView):
    model = Video
    fields = ["name", "url", "start", "end", "tags"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class VideoDelete(StaffRequiredMixin, DeleteView):
    model = Video
    success_url = reverse_lazy("signage:video_list")


class VideoUpdate(StaffRequiredMixin, UpdateView):
    model = Video
    fields = ["name", "url", "start", "end", "tags"]
