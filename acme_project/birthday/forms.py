from django import forms

from django.core.exceptions import ValidationError

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]


    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        full_name = first_name + ' ' + last_name
        if full_name in BEATLES:
            raise ValidationError('Битлы в пролете.\nНазовитесь по другому.')
        if full_name == 'Владимир Путин':
            raise ValidationError('Путин - президент России!')





