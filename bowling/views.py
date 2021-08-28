from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from bowling.models import Row, RowSession, Player, PersonalFrame, PersonalThrow
from bowling.forms import RowSessionCreateForm, PlayerForm, PersonalFrameForm, PersonalThrowForm


def make_throws(request, pk):
    if request.is_ajax and request.method == "POST":
        data = request.POST
        player_pk = int(data.get("player"))
        frame_name = data.get("frame_name")
        player = Player.objects.get(pk=player_pk)
        frame = PersonalFrame.objects.create(name=frame_name, player=player)
        throw_1 = data.get("throw_1")
        throw_2 = data.get("throw_2")
        if throw_1 == "X":
            PersonalThrow.objects.create(
                frame=frame,
                name="Throw Strike",
                value=throw_1,
            )
            return JsonResponse({"status":"success"})
        if throw_2 == "/":
            PersonalThrow.objects.create(
                frame=frame,
                name="Throws Spare",
                value=throw_1,
            )
            return JsonResponse({"status":"success"})
        PersonalThrow.objects.create(
            frame=frame,
            name="Throw one",
            value=throw_1,
        )
        PersonalThrow.objects.create(
            frame=frame,
            name="Throw two",
            value=throw_2,
        )
        return JsonResponse({"status":"success"})



# Create your views here.
class RowListView(ListView):

    template_name = "row_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of rows",
            })
        print(dict(context))
        return context


class RowDetailView(DetailView):

    template_name = "row_detail.html"
    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class RowSessionDetailView(DetailView):

    template_name = "row_session_detail.html"

    model = RowSession

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class RowSessionUpdateView(UpdateView):

    template_name = "row_session_update.html"
    model = RowSession
    form_class = RowSessionCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = context["object"]
        players = object.players.all()
        if object.players.all():
            list_of_entry = [[entry, PlayerForm(instance=entry)] for entry in players]
            context.update({"list_of_entry": list_of_entry})
        context.update({"player_form": PlayerForm})
        print(context)
        return context


class RowSessionCreateView(CreateView):

    template_name = "row_session_create.html"

    model = RowSession
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row, "user":user}
        return super().get(request, *args, **kwargs)


class PlayerUpdateView(UpdateView):

    template_name = "row_session_update.html"
    model = Player
    form_class = PlayerForm


class PersonalFrameListView(ListView):
    template_name = "personal_frame_list.html"

    model = PersonalFrame
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of personal frames",
            "list_len": len(context["personalframe_list"])
        })
        return context


class PersonalFrameDetailView(DetailView):
    """docstring for CarDetailView."""
    template_name = "personal_frame_detail.html"
    model = PersonalFrame

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PlayerCreateView(CreateView):

    template_name = "player_create.html"

    model = Player
    form_class = PlayerForm


class PlayerListView(ListView):
    template_name = "player_list.html"

    model = Player
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of players",
            "list_len": len(context["player_list"])
        })
        return context


class PlayerDetailView(DetailView):
    """docstring for CarDetailView."""
    template_name = "player_detail.html"
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PersonalFrameCreateView(CreateView):
    template_name = "personal_frame_create.html"

    model = PersonalFrame
    form_class = PersonalFrameForm


class PersonalThrowListView(ListView):
    template_name = "personal_throw_list.html"

    model = PersonalThrow
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of personal throws",
            "list_len": len(context["personalthrow_list"])
        })
        return context


class PersonalThrowDetailView(DetailView):
    """docstring for CarDetailView."""
    template_name = "personal_throw_detail.html"
    model = PersonalThrow

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


