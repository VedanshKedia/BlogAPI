# from django.core.files.images import get_image_dimensions
from django import forms
# from django.contrib.auth.models import User
from .models import Profile

# BIRTH_YEAR_CHOICES = [str(year) for year in range(1980, 2005)]
# MONTH_CHOICES = [str(month) for month in range(1, 13)]
# DATE_CHOICES = [str(date) for date in range(1, 32)]

BIRTH_YEAR_CHOICES = ['2011','2013','2014']
MONTH_CHOICES = {
    1: ('jan'), 2: ('feb'), 3: ('mar'), 4: ('apr'),
    5: ('may'), 6: ('jun'), 7: ('jul'), 8: ('aug'),
    9: ('sep'), 10: ('oct'), 11: ('nov'), 12: ('dec')
}


class ProfileDetailsForm(forms.ModelForm):
    # username = forms.CharField(max_length=50)
    avatar = forms.ImageField()
    emailid = forms.EmailField()
    number = forms.CharField(max_length=10)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, months=MONTH_CHOICES))

    # class Meta:
    #     model = Profile
    #     fields = ['avatar', 'emailid', 'number', 'dob']

    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']
    #
    #     try:
    #         # w, h = get_image_dimensions(avatar)
    #
    #         # validate dimensions
    #         # max_width = max_height = 100
    #         # if w > max_width or h > max_height:
    #         #     raise forms.ValidationError(
    #         #         u'Please use an image that is '
    #         #          '%s x %s pixels or smaller.' % (max_width, max_height))
    #
    #         # validate content type
    #         main, sub = avatar.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise forms.ValidationError(u'Please use a JPEG, '
    #                                         'GIF or PNG image.')
    #
    #         # validate file size
    #         if len(avatar) > (1 * 1024 * 1024):
    #             raise forms.ValidationError(
    #                 u'Avatar file size may not exceed 1MB.')
    #
    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass
    #
    #     return avatar


# class ProfileDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['emailid', 'number', 'dob']
