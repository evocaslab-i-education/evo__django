import uuid

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse_lazy


class ColorsChoices(models.TextChoices):
    BLACK = "black", "Black"
    WHITE = "white", "White"
    RED = "red", "Red"


class Color(models.Model):
    name = models.CharField("Name", help_text="Name of color", max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"humans/avatars/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Human(models.Model):
    name = models.CharField("Name", help_text="It is name of human", max_length=200)
    age = models.PositiveSmallIntegerField("Age", help_text="How old this human", validators=[MaxValueValidator(150)])

    avatar = models.ImageField(
        "Avatar",
        upload_to=get_icon_path,
        max_length=255,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    favourite_color = models.CharField(
        "Favourite color",
        max_length=32,
        choices=ColorsChoices.choices,
        default=ColorsChoices.WHITE,
    )

    favourite_color_by_foreign_key = models.ForeignKey(
        Color,
        related_name="humans_related_by_foreign_key",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    favourite_color_many_to_many = models.ManyToManyField(
        Color,
        related_name="humans_related_by_many_to_many",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    __repr__ = __str__

    # def __repr__(self) -> str:
    #     return str(self)

    def get_absolute_url(self):
        return reverse_lazy("humans:edit", kwargs={"pk": self.pk})


class SuperHuman(Human):
    level = models.PositiveIntegerField("Level", help_text="Level of power")
