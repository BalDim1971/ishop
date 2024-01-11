"""
Описание форм по работе с товарами
"""

from django import forms

from catalog.models import Product, VersionProduct

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
              'радар']


class StyleFormMixin:
    '''
    Общий класс для стилизации форм
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for i in stop_words:
            if i in name:
                raise forms.ValidationError('Эти товары запрещены!')
        
        return name
    
    def clean_description(self):
        name = self.cleaned_data['description'].lower()
        for i in stop_words:
            if i in name:
                raise forms.ValidationError('Эти темы запрещены!')
        
        return name


class VersionForm(StyleFormMixin, forms.ModelForm):
    
    class Meta:
        model = VersionProduct
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'version_flag':
                field.widget.attrs['class'] = 'form-control'
