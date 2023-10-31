from django.forms import ModelForm
from .models import CookingEvent

class CookingEventForm(ModelForm):
  class Meta:
    model = CookingEvent
    fields = ['date', 'notes']