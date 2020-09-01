from django import forms
from .models import Meal

# class OrderForm(forms.Form):
#     mainDish = forms.CharField(label="Main Dish", max_length=100)
#     sideDish = forms.CharField(label="Side Dish", max_length=100)
#     typeOfRice = forms.ChoiceField(label="Type Of Rice", choices=[('Fried Rice', 'Fried Rice'), ('Steamed Rice', 'Steamed Rice')])

class OrderForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['mainDish', 'sideDish', 'rice']
        labels = {'mainDish' : 'Main Dish', 'sideDish' : 'Side Dish', 'rice' : "Type Of Rice"}

class MultipleMealForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=7)
