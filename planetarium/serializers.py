from django.db import transaction
from rest_framework import serializers

from planetarium.models import (
    Ticket,
    ShowTheme,
    PlanetariumDome,
    AstronomyShow,
    Reservation,
    ShowSession
)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "show_session", "reservation")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name")


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row", "size")


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_theme")


class AstronomyShowListSerializer(AstronomyShowSerializer):
    show_theme = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class AstronomyShowRetrieveSerializer(AstronomyShowSerializer):
    show_theme = ShowThemeSerializer(many=True)


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "tickets")

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            reservation = Reservation.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(reservation=reservation, **ticket_data)
            return reservation


class ShowSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetarium_dome", "show_time")


class ShowSessionListSerializer(serializers.ModelSerializer):
    astronomy_show_title = serializers.CharField(source="astronomy_show.title", read_only=True)
    astronomy_show_description = serializers.CharField(source="astronomy_show.description", read_only=True)

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show_title", "astronomy_show_description", "planetarium_dome", "show_time")


class ShowSessionRetrieveSerializer(ShowSessionSerializer):
    astronomy_show = AstronomyShowRetrieveSerializer(many=False, read_only=True)
    planetarium_dome = PlanetariumDomeSerializer(many=False, read_only=True)
