from django.contrib import admin
from planetarium.models import (
    ShowSession,
    ShowTheme,
    AstronomyShow,
    Reservation,
    Ticket,
    PlanetariumDome
)

admin.site.register(ShowSession)
admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(Reservation)
admin.site.register(Ticket)
admin.site.register(PlanetariumDome)
