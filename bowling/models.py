from django.db import models
from django.urls import reverse
# from bowling.forms import PlayerForm
# Create your models here.
class Row(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('row-list')

class RowSession(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
        )
    row = models.ForeignKey(
        "bowling.Row",
        on_delete=models.CASCADE,
        related_name="row_sessions"
    )
    date = models.DateField()

    @property
    def display_username(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('row_session-detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return f"{self.user.username} {self.pk}"

class Player(models.Model):
    """docstring for Player."""

    name = models.CharField(max_length=100)
    last_update = models.DateField()
    row = models.ForeignKey(
        "bowling.RowSession",
        on_delete=models.CASCADE,
        related_name="players"
    )

    # def get_form(self, initial=None):
    #     if initial:
    #         return PlayerForm(initial=initial)
    #     return PlayerForm()

    @property
    def score(self):
        return "0"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'pk': self.pk})


class PersonalFrame(models.Model):

    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        "bowling.Player",
        on_delete=models.CASCADE,
        related_name="frames"
    )

    def __str__(self):
        return self.name

    def frame_sum(self):
        throws = self.throws.all()
        collect_list = [int(i) for i in throws]
        return sum(collect_list)

    def get_absolute_url(self):
        return reverse('personal_frame-detail', kwargs={'pk': self.pk})


class PersonalThrow(models.Model):

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=2)
    frame = models.ForeignKey(
        "bowling.PersonalFrame",
        on_delete=models.CASCADE,
        related_name="throws"
    )

    def __int__(self):
        if str(self.value).isdigit():
            return int(self.value)
        return 0

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('personal_throw-detail', kwargs={'pk': self.pk})
