from django import forms
from catagory.models import Catagory
from .models import Book
class BookForm(forms.Form):
    title =forms.CharField(max_length=100,required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    price = forms.DecimalField(max_digits=10,decimal_places=2)
    image = forms.ImageField(label="Cover Image")
    Catagory=forms.ChoiceField(choices=[(cat.id,cat.name) for cat in Catagory.objects.all()])

class BookFormModel(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('id','update_date')