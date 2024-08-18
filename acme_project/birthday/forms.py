from django import forms

from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        exclude = ('author', )
        # fields = '__all__'
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
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError('Битлы в пролете.\nНазовитесь по другому.')
        if full_name == 'Владимир Путин':
            send_mail(
                subject='Внимание!!! Путин!!!',
                message=f'{first_name} {last_name} опубликовал запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError('Путин - президент России!')





