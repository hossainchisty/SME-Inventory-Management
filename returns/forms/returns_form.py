from django.forms import ModelForm

from returns.models import Return


class ReturnForm(ModelForm):
    ''' Form asking for the returns Information '''
    class Meta:
        model = Return
        fields = '__all__'
        exclude = ('user',)
