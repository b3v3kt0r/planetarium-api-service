from django.contrib import admin
from planetarium.models import (
    ShowSession,
    ShowTheme,
    AstronomyShow,
    Reservation,
    Ticket,
    PlanetariumDome,
)


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


class ReservationAdmin(admin.ModelAdmin):
    inlines = [TicketInline]


admin.site.register(ShowSession)
admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Ticket)
admin.site.register(PlanetariumDome)
