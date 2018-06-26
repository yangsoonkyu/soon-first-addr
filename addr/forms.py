from django import forms

from .models import Friend

class FriendForm(forms.ModelForm):

    class Meta:
        model = Friend
        fields = ('name', 'phon_number_1', 'phon_number_2', 'e_mail',)