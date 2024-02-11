from django import forms

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = '__all__'
           
# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid characters")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label='Enter First Name', validators=[validate_comma])
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)
    
    # def clean_first_name(self):
    #     data =self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data
    # def clean_last_name(self):
    #     data =self.cleaned_data['last_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid Last Name")
    #     return data