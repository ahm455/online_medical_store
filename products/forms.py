from django import forms
from .models import Medicine, ordereditems,Customer,order

class medicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine_name', 'potency', 'cost_price', 'selling_price']

from django import forms
from .models import order, ordereditems, Customer, Medicine

class OrderedItemsForm(forms.ModelForm):
    class Meta:
        model = ordereditems
        fields = ['customer', 'medicine', 'quantity']

OrderedItemsFormSet = forms.inlineformset_factory(
    order, ordereditems, form=OrderedItemsForm,
    extra=1, can_delete=True
)

class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ['customer']       

from django import forms
from django.contrib.auth.models import User
from .models import Customer

class customerForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['name', 'age', 'phone', 'username', 'email', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
    
        customer = super().save(commit=False)
        customer.user = user
        if commit:
            customer.save()
        return customer