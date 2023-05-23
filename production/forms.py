from .models import JiggerProduction

from django import forms


class JiggerPrdInputForm(forms.ModelForm):
    production_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    # item = forms.CharField(widget=forms.TextInput(
    #     attrs={"class": "dksdkfdfhdfh"}), validators=[0, 1, 2])

    class Meta:
        model = JiggerProduction
        fields = ['item', 'machine', 'shift', 'quantity',
                  'forming_loss', 'production_date']


# class jiggerFormSet(forms.formset_factory(form=JiggerPrdInputForm, extra=40)):
#     production_date = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}))

#     class Meta:
#         model = JiggerProduction
#         fields = ['item', 'machine', 'shift', 'quantity',
#                   'forming_loss']
