from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Custom
from .forms import BlogForm, Custom_Image_Form
from .serializers import BlogPostSerializer
from datetime import datetime
from rest_framework import viewsets
from . import models
from . import serializers


class CustomViewset(viewsets.ModelViewSet):
    queryset = models.Custom.objects.all()
    serializer_class = serializers.CustomSerializer


class BlogPostViewset(viewsets.ModelViewSet):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer


def profile_form(request):

    # profile = Custom_Image_Form(user=request.user)

    if request.method == 'POST':
        p_form = Custom_Image_Form(request.POST,
                                   request.FILES,
                                   instance=request.user.custom)
        # u_form = UserUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid():
            # u_form.save()
            p_form.save()

            return redirect('blogs')

    else:
        p_form = Custom_Image_Form(instance=request.user.custom)

    context = {
        'p_form': p_form
    }

    return render(request,'custom_profile_form.html', context)


@login_required()
def blog_form(request):
    if request.method == 'POST':
        form_b = BlogForm(request.POST)

        if form_b.is_valid():

            title = form_b.cleaned_data['title']
            content = form_b.cleaned_data['content']

            print("check the values assigned", Custom.objects.filter(me=request.user.username))

            blog_data = BlogPost.objects.create(
                blogger=Custom.objects.filter(me=request.user.username),
                title=title,
                content=content,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )

            print('\n\n\n check the data=\n', blog_data)

            blog_data.save()

            return HttpResponseRedirect(reverse('blogs'))
        else:
            return render(request, 'upload_blog_form.html', {'form_b': form_b})

    else:
        form_b = BlogForm()

        return render(request, 'upload_blog_form.html', {'form_b': form_b})


def blogs(request):

    blog = BlogPost.objects.all()

    return render(request, 'blogs.html', {'blog': blog})

