# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

# from userprofile.models import Profile
from .forms import ProfileDetailsForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# from blogs import urls

# Create your views here.

# def profileimageform(request):



@login_required()
def profileview(request):
    userdata = Profile.objects.all()
    # username = userdata.username
    # emailid = userdata.ema
    # if userdata.exists():
    #     print(userdata)
    # else:
    #     print("user doest not exist")
    # print(userdata)
    if userdata:
        return render(request, template_name='user_profile.html', context={'userdata': userdata})
    else:
        return HttpResponseRedirect(reverse('user_profile_edit'))


# @login_required()
# def profileimageform(request):
#     if request.method == 'POST':
#         form1 = ProfileImageForm(request.POST, request.FILES)
#         form2 = ProfileDetailsForm()
#
#         if form1.is_valid():
#             form1.save()
#             return HttpResponseRedirect(reverse('user_profile'))
#         # if form2.is_valid():
#         #     form1.save()
#         #     return HttpResponseRedirect(reverse('userdata'))
#     else:
#         form1 = ProfileImageForm()
#         form2 = ProfileDetailsForm()
#     return render(request, 'user_profile_edit.html', {'form1': form1, 'form2': form2})


@login_required()
def profiledetailsform(request):
    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, request.FILES)
        # form1 = ProfileImageForm()

        if form.is_valid():
            # print(form.save(commit=False))
            image = form.cleaned_data['avatar']
            email = form.cleaned_data['emailid']
            dob = form.cleaned_data['dob']
            number = form.cleaned_data['number']

            prof: Profile = Profile.objects.create(
                # username=request.user,
                avatar=image,
                emailid=email,
                dob=dob,
                number=number,
            )

            print('output:' + str(prof.save()))

            return HttpResponseRedirect(reverse('user_profile'))
    else:
        form = ProfileDetailsForm(request.GET)
        return render(request, 'user_profile_edit.html', {'form': form})
        # form1 = ProfileImageForm()


@login_required()
def success(request):
    return HttpResponse('successfuly uploaded')




