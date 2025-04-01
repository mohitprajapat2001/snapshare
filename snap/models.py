from django.db.models import ImageField, ForeignKey, CharField, CASCADE
from django_extensions.db.models import TimeStampedModel
from django.conf import settings
from random import random
from string import ascii_letters
from django.urls import reverse
from snap.constants import SNAP_UPLOAD_PATH_USER, SNAP_UPLOAD_PATH_NO_USER, Verbose


def _generate_random_unique_snap_name():
    """
    Generates a random and unique name for the snap. format 9 characters alphabet

    :param self: Snap
    :return: str
    """
    while True:
        name = "".join(
            [ascii_letters[int(random() * len(ascii_letters))] for _ in range(9)]
        )
        if not Snap.objects.filter(snap=name).exists():
            return name


def _upload_to(self, filename: str):
    """
    Uploads the file to the user's folder.

    :param self: Snap
    :param filename: str
    :return: str
    """
    if self.user:
        return SNAP_UPLOAD_PATH_USER % (self.user.username, filename)
    return SNAP_UPLOAD_PATH_NO_USER % filename


class Snap(TimeStampedModel):
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name="snaps",
    )
    image = ImageField(upload_to=_upload_to)
    snap = CharField(max_length=12, default=_generate_random_unique_snap_name)

    class Meta:
        verbose_name = Verbose.SNAP
        verbose_name_plural = Verbose.SNAPS

    def __str__(self):
        return self.snap

    def get_absolute_url(self):
        return reverse("snap:view", kwargs={"snap": self.snap})

    def get_detail_url(self):
        return reverse("snap:detail", kwargs={"snap": self.snap})
