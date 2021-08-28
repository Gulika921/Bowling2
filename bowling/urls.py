from django.urls import path
from bowling.views import (
    RowListView,
    RowDetailView,
    RowSessionDetailView,
    RowSessionCreateView,
    RowSessionUpdateView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerListView,
    PlayerDetailView,
    PersonalFrameCreateView,
    PersonalFrameListView,
    PersonalFrameDetailView,
    PersonalThrowDetailView,
    PersonalThrowListView,
    make_throws,
)
urlpatterns = [
    path(
        "row/",
        RowListView.as_view(),
        name="row-list"
    ),
    path(
        "row/<int:pk>",
        RowDetailView.as_view(),
        name="row-detail"
    ),
    path(
        "row_session/create",
        RowSessionCreateView.as_view(),
        name="row_session-create"
    ),
    path(
        "row_session/<int:pk>/update",
        RowSessionUpdateView.as_view(),
        name="row_session-update"
    ),
    path(
        "row_session/<int:pk>",
        RowSessionDetailView.as_view(),
        name="row_session-detail"
    ),
    path(
        "row_session/<int:pk>/throws",
        make_throws,
        name="row_session-throws"
    ),
    path(
        "player/create",
        PlayerCreateView.as_view(),
        name="player-create"
    ),
    path(
        "player/<int:pk>/update",
        PlayerUpdateView.as_view(),
        name="player-update"
    ),
    path(
            "player/",
            PlayerListView.as_view(),
            name="player-list"
        ),
        path(
            "player/<int:pk>",
            PlayerDetailView.as_view(),
            name="player-detail"
        ),
    path(
        "personal_frame/",
         PersonalFrameListView.as_view(),
         name="personal_frame-list"
        ),
    path(
            "personal_frame/create",
            PersonalFrameCreateView.as_view(),
            name="personal_frame-create"
        ),
    path(
            "personal_frame/<int:pk>",
             PersonalFrameDetailView.as_view(),
             name="personal_frame-detail"

        ),
    path(
        "personal_throw/",
         PersonalThrowListView.as_view(),
         name="personal_throw-list"
         ),
    path("personal_throw/<int:pk>",
         PersonalThrowDetailView.as_view(),
         name="personal_throw-detail"
         ),
]