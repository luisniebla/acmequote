from django.urls import path

from . import views

urlpatterns = [
    path("<uuid:resource_id>", views.index, name="quote"),
]
