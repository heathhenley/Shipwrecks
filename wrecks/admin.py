from django.contrib import admin
from django.db.models.functions import Lower

from .models import Wreck

@admin.register(Wreck)
class WreckAdmin(admin.ModelAdmin):
    search_fields = ["vessel_name"]

    def get_ordering(self, request):
      return [Lower("vessel_name")]