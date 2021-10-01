from django import forms


class CallForm(forms.Form):
    subject = forms.CharField(label='Номер Вашего телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))