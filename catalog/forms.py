"""
Описание форм по работе с товарами
"""

from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def clean_name(self):
        stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                      'радар']
        name = self.cleaned_data['name'].lower()
        for i in stop_words:
            if i in name:
                raise forms.ValidationError('Эти товары запрещены')

        return name
