from django.shortcuts import render
from .forms import OrderForm, MultipleMealForm
from django.forms import formset_factory
from .models import Meal

# Create your views here.
def home(request):
    return render(request, 'cuisine/home.html')

def order(request):
    multipleMealForm = MultipleMealForm()

    if request.method == 'POST':
        filledForm = OrderForm(request.POST)
        if filledForm.is_valid():
            createdMeal = filledForm.save()
            createdMealPk = createdMeal.id
            note = 'Thank you for ordering! Your %s anb %s with %s is on it way!' %(filledForm.cleaned_data['mainDish'],
                                                                             filledForm.cleaned_data['sideDish'],
                                                                             filledForm.cleaned_data['rice'],)
            filledForm = OrderForm()
        else:
            createdMealPk = None
            note = 'Order was not created properly, try again.'
        return render(request, 'cuisine/order.html', {'created_meal_pk' : createdMealPk, 'orderForm' : filledForm, 'note' : note, 'multiple_meal' : multipleMealForm})

    else:
        form = OrderForm()
        return render(request, 'cuisine/order.html', {'orderForm' : form, 'multiple_meal' : multipleMealForm})

def meals(request):
    numberOfMeals = 2
    filledMulpitalMealForm = MultipleMealForm(request.GET)
    if filledMulpitalMealForm.is_valid():
        numberOfMeals = filledMulpitalMealForm.cleaned_data['number']
    MealFormSet = formset_factory(OrderForm, extra=numberOfMeals)
    formset = MealFormSet()
    if request.method == 'POST':
        filledFormSet = MealFormSet(request.POST)
        if filledFormSet.is_valid():
            # for form in filledFormSet:
            #     print(form.cleaned_data['mainDish'])
            note = "Meals have been ordered"
        else:
            note = "Order was not created, please try again."
        return render(request, 'cuisine/meals.html', {'note' : note, 'formset' : formset})

    else:
        return render(request, 'cuisine/meals.html', {'formset' : formset})

def editOrder(request, pk):
    """Edit created order by its primary key"""
    order = Meal.objects.get(pk=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        filledForm = OrderForm(request.POST, instance=order)
        if filledForm.is_valid():
            filledForm.save()
            form = filledForm
            note = "Your order has been updated."
            return render(request, 'cuisine/editOrder.html', {'orderForm' : form, 'order' : order, 'note' : note})
    return render(request, 'cuisine/editOrder.html', {'orderForm' : form, 'order' : order})
