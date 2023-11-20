from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "picture", "category", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        denied_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        cleaned_data_lower_case = str(self.cleaned_data.get('title')).lower()
        cleaned_data = self.cleaned_data.get('title')

        for tested_word in denied_words:
            if tested_word in cleaned_data_lower_case:
                raise forms.ValidationError(f"Нельзя использовать в наименовании слово {tested_word}")

        return cleaned_data

class ProductFormForModerator(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["description", "category", "is_published"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ["nomer", "version_title", "current_version"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'current_version':
                field.widget.attrs['class'] = 'form-control'
