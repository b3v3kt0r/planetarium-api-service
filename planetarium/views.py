from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from planetarium.models import (
    ShowTheme,
    ShowSession,
    AstronomyShow,
    Reservation,
    Ticket,
    PlanetariumDome
)
from planetarium.serializers import (
    ShowThemeSerializer,
    ShowSessionSerializer,
    AstronomyShowSerializer,
    ReservationSerializer,
    TicketSerializer,
    PlanetariumDomeSerializer, ShowSessionListSerializer, AstronomyShowListSerializer
)


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AstronomyShowListSerializer
        else:
            return AstronomyShowSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.prefetch_related("show_theme")
        else:
            return queryset


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ShowSessionListSerializer
        else:
            return ShowSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.select_related()
        else:
            return queryset


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
