from django import forms
from .models import Item, Cashier, Store, Check, Sale
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'name': 'Название товара',
        }


class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = ['name', 'phone_number']
        labels = {
            'name': 'Имя кассира',
            'phone_number': 'Номер телефона кассира',
        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address']
        labels = {
            'name': 'Название магазина',
            'address': 'Адрес магазина',
        }


class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['cashier', 'date_time', 'total_sum', 'store']
        labels = {
            'cashier': 'Кассир',
            'date_time': 'Дата и время',
            'total_sum': 'Общая сумма',
            'store': 'Магазин',
        }
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'total_sum': forms.NumberInput(attrs={
                'step': 10,
                'min': 0,
                'max': 999999,
                'decimal_places': 2,
            })
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['check_id', 'item', 'quantity']
        labels = {
            'check_id': 'ID чека',
            'item': 'Товар',
            'quantity': 'Количество',
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']