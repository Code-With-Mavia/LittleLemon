from django import forms
from .models import Booking

# Generate choices for slots: 10:00 to 19:00
SLOT_CHOICES = [(i, f"{i}:00") for i in range(10, 20)]

class BookingForm(forms.ModelForm):
    reservation_slot = forms.ChoiceField(choices=SLOT_CHOICES, label="Reservation Time")

    class Meta:
        model = Booking
        fields = ["first_name", "last_name", "guest_number", "comment", "reservation_date", "reservation_slot"]
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
