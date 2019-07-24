from django import forms


from blogs.models import Custom, BlogPost
from django.core.validators import FileExtensionValidator, RegexValidator


class Custom_Image_Form(forms.ModelForm):
    avatar = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+919999999999'. Utpo 10 digits")
    number = forms.CharField(validators=[phone_regex], max_length=10)

    class Meta:
        model = Custom
        fields = ['avatar', 'number']

    def clean_avatar(self):

        avatar = self.cleaned_data['avatar']

        if avatar:

            if avatar.size > (1 * 1024 * 1024):
                raise forms.ValidationError("Max size Allowed is 1MB")

        return avatar


class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=10000)

    class Meta:
        model = BlogPost
        fields = ['title', 'content']
