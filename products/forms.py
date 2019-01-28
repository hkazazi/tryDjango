from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class':'new-class-name two',
                'rows':5,
                'cols':5,

                }
                                             ))
    price= forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        if 'a' in title:
            return title
        else:
            raise forms.ValidationError('hellllow')


# class RawProductForm(forms.Form):
#
#     title = forms.CharField()
#     description = forms.CharField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 'class':'new-class-name two',
#                 'rows':5,
#                 'cols':5,
#
#                 }
#                                              ))
#     price= forms.DecimalField(initial=199.99)