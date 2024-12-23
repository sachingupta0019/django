from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect ,HttpResponse
from .models import BlogPost
from .forms import UserRegistrationForm, UserLoginForm, BlogCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.db.models import Q

# Create your views here.
def home(request):
    post = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'post' : post})

# About-US
def about_us(request):
    return render(request, 'blog/about-us.html')

# Contact-US
def contact_us(request):
    return render(request, 'blog/contact-us.html')

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        post = BlogPost.objects.all()
        user = request.user
        full_name = user.get_full_name()
        return render(request, 'blog/dashboard.html',{'post' : post, 'full_name' : full_name})
    else:
        return HttpResponseRedirect('/login/')
    
def viewPost(request, slug = None):
    if request.user.is_authenticated:
        view_post = get_list_or_404(BlogPost, post_slug = slug)
        return render(request,'blog/post/viewpost.html',{'view_post': view_post})
    else:
        view_post = get_list_or_404(BlogPost, post_slug = slug)
        return render(request,'blog/post/viewpost.html',{'view_post': view_post})

# Blog Post Search results Page View
def search_post(request):
    search_query = request.GET.get('q')
    if search_query:
        results = BlogPost.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query))
    else:
        results = []
    return render(request, 'blog/post/search_blog.html', {'search_query' : search_query,'search_results' : results})

# User Registration
def user_registration(request):
    if request.method == "POST":
        user_register = UserRegistrationForm(request.POST)
        if user_register.is_valid():
            user_register.cleaned_data
            messages.success(request, 'Welcome to PostsVault.')
            user = user_register.save()
            group = Group.objects.get(name = 'Author')
            user.groups.add(group)
            return HttpResponseRedirect('/login/')
        # else:
        #     messages.error(request, 'Somethign went wrong!')
    else:
        user_register = UserRegistrationForm()
    return render(request, 'user/registration.html',{'register' : user_register})

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user_form = UserLoginForm(request=request, data = request.POST)
            if user_form.is_valid():
                uname = user_form.cleaned_data['username']
                upass = user_form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in Successfully!')
                    return HttpResponseRedirect('/dashboard/')
                # else:
                #     messages.info(request,'You are not registered with us! Please Signup.')
                #     return HttpResponseRedirect('/signup/')
            else:
                messages.info(request, 'Invalid User.')
        else:
            user_form = UserLoginForm()
        return render(request, 'user/login.html', {'user' : user_form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Create New Blog Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addBlog = BlogCreationForm(request.POST, request.FILES)
            if addBlog.is_valid():
                title = addBlog.cleaned_data['title']
                desc = addBlog.cleaned_data['excerpt']
                content = addBlog.cleaned_data['content']
                thumbnail = addBlog.cleaned_data['post_thumbnail']
                image = addBlog.cleaned_data['post_image']
                tag = addBlog.cleaned_data['post_tag']
                author = addBlog.cleaned_data['author_name'] 
                blog = BlogPost(title = title, excerpt = desc, content = content, post_thumbnail = thumbnail,post_image = image,post_tag = tag,author_name = author)
                messages.success(request, 'Blog Created Successfully!')
                blog.save() 
                return HttpResponseRedirect('/')
                # return HttpResponseRedirect(f'/blog/{blog.slug}/') 
            else:
                messages.error(request,'Something Went wrong! Please try again later.')
                print(addBlog.errors)
                return render(request, 'blog/post/addpost.html', {'NewBlog': addBlog})
                
        else:
            addBlog = BlogCreationForm()
            return render(request,'blog/post/addpost.html',{'NewBlog' : addBlog})
    else:
        return HttpResponseRedirect('/login/')

# Edit Blog Post
def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            blog = BlogPost.objects.get(pk = id)
            edit_blog = BlogCreationForm(request.POST, request.FILES, instance = blog )
            if edit_blog.is_valid():
                edit_blog.cleaned_data
                edit_blog.save()
                return HttpResponseRedirect('/')
            else:
                return render(request, 'blog/post/editpost.html', {'edit_blog': edit_blog})
        else:
            blog = BlogPost.objects.get( pk = id)
            edit_blog = BlogCreationForm(instance=blog)
            return render(request,'blog/post/editpost.html', {'edit_blog' : edit_blog})
    else:
        messages.info(request, "Login to Edit Post")
        return HttpResponseRedirect('/login/')

# Delete Blog Post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            blog = BlogPost.objects.get(pk=id)
            blog.delete()
            return HttpResponseRedirect('/dashboard/')  
        else:
            messages.error(request,'You are not Authorized to delete!!!!!')
            return render(request, 'blog/post/error.html')
    else:
        return HttpResponseRedirect('/login/')