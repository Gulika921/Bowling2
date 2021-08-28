from django import forms
from bowling.models import RowSession, Row, Player, PersonalFrame, PersonalThrow
from django.contrib.auth.models import User


class RowSessionCreateForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=User.objects.all())
    row = forms.ModelChoiceField(queryset=Row.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    # vin_number = forms.CharField(max_length=100)

    class Meta:
        model = RowSession
        fields = "__all__"


class PlayerForm(forms.ModelForm):

    last_update = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )

    class Meta:
        model = Player
        fields = "__all__"


class PersonalFrameForm(forms.ModelForm):

    # name = forms.CharField(max_length=100)
    player = forms.ModelChoiceField(queryset=Player.objects.all())

    class Meta:
        model = PersonalFrame
        fields = "__all__"


class PersonalThrowForm(forms.Form):

    # name = forms.CharField(max_length=100)
    # value = models.CharField(max_length=2)
    frame = forms.ModelChoiceField(queryset=PersonalThrow.objects.all())

    class Meta:
        model = PersonalThrow
        fields = "__all__"
