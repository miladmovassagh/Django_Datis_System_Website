from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','phone_number','age','national_code','city','address','postal_code')
        fields = ('first_name','last_name','username','email','phone_number','city','address','postal_code','password1','password2')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['first_name'].widget.attrs["required"] = "required"
        self.fields['last_name'].widget.attrs["required"] = "required"
        # print(self.fields)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields