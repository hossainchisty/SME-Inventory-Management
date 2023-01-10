# from ckeditor.widgets import CKEditorWidget

from django.forms import ModelForm

from product.models import Product


class ProductForm(ModelForm):
    ''' Form asking for create products '''
    # product_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user', ]
