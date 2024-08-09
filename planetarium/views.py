from django.db.models import Count, F, IntegerField, ExpressionWrapper
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
    PlanetariumDomeSerializer,
    ShowSessionListSerializer,
    AstronomyShowListSerializer, AstronomyShowRetrieveSerializer, ShowSessionRetrieveSerializer
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
        elif self.action == "retrieve":
            return AstronomyShowRetrieveSerializer
        else:
            return AstronomyShowSerializer

    def get_queryset(self):
        queryset = self.queryset

        show_theme = self.request.query_params.get("show_theme")
        if show_theme:
            queryset = queryset.filter(show_theme__name__icontains=show_theme)

        if self.action in ["list", "retrieve"]:
            queryset.prefetch_related("show_theme")

        return queryset.distinct()


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ShowSessionListSerializer
        elif self.action == "retrieve":
            return ShowSessionRetrieveSerializer
        else:
            return ShowSessionSerializer

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.select_related("planetarium_dome", "astronomy_show")

        if self.action == "list":
            queryset = queryset.annotate(
                dome_capacity=ExpressionWrapper(
                    F("planetarium_dome__rows") * F("planetarium_dome__seats_in_row"),
                    output_field=IntegerField()
                ),
                tickets_available=ExpressionWrapper(
                    F("planetarium_dome__rows") * F("planetarium_dome__seats_in_row") - Count("tickets"),
                    output_field=IntegerField()
                )
            )

        elif self.action == "retrieve":
            queryset = queryset.prefetch_related("tickets")

        return queryset.distinct()


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
