from django import forms

from .models import Product


class ProductModelForm(forms.ModelForm):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your title"})) 
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
                attrs={
                    "placeholder":"Enter your description...",
                    "class":"new-class-name two",
                    "id":"my-id-for-textarea",
                    "rows":20,
                    "cols":120
                }
            )
        )
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "good" in title: # Check if title field contains word "good"
            return title
        if title.endswith("lol"):
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Enter your title..."}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
                attrs={
                    "placeholder":"Enter your description...",
                    "class":"new-class-name two",
                    "id":"my-id-for-textarea",
                    "rows":20,
                    "cols":120
                }
            )
        )
    price = forms.DecimalField(initial=199.99)
