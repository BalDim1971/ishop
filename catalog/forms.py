"""
Описание форм по работе с товарами
"""

from django import forms

from catalog.models import Product, VersionProduct, Category

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
              'радар']


class StyleFormMixin:
    """
    Общий класс для стилизации форм
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['version_sign', 'is_published']:
                field.widget.attrs['class'] = 'form-control'


class CategoryForm(StyleFormMixin, forms.ModelForm):
    """
    Класс с описанием формы для категорий
    """
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """
    Класс с описанием формы для товара
    """
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
    """
    Класс с описанием формы для версии товара
    """
    class Meta:
        model = VersionProduct
        fields = '__all__'
    

class ModeratorForm(StyleFormMixin, forms.ModelForm):
    """
    Класс с описанием формы товара для модератора ?
    """
    class Meta:
        model = Product
        fields = ('description', 'category', 'status',)
