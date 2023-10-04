from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from . forms import *
from django.http import HttpResponseForbidden

# Create your views here.


def loginView(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Get Django Login Form and fill it with user's data coming from POST request
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
# Validate username and password (user credentials)
            user = authenticate(username=username, password=password)
# If the user is authenticated
            if user is not None:
                # This User will be logged in and will be
                login(request, user)
        # Will be Redirected to Home page showing a success message
                return redirect("posts")

    return render(request, "BlogApplication/LoginPage.html", context={"form": form})


def index(request):
    context = {'posts': BlogPost.objects.all()}
    return render(request, 'BlogApplication/Home.html', context)


def editPost(request, pk):

    post = BlogPost.objects.get(id=pk)
    # if request.user == post.author or request.user == request.user.is_superuser:
    form = BlogPostForm(instance=post)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'postID': pk}
    return render(request, 'BlogApplication/Edit.html', context)
    # else:
    # return HttpResponseForbidden("You are not authorized to edit this post.")


def deletePost(request, pk):
    obj = BlogPost.objects.get(id=pk)
    # if request.user == obj.author or request.user == request.user.is_superuser:
    obj.delete()
    return redirect("posts")
    # else:
    return HttpResponseForbidden("You are not authorized to delete this post.")


def addPost(request):
    context = {'success': False}

    if request.method == 'POST':
        _title = request.POST['title']
        _content = request.POST['content']
        _category = request.POST['category']

        if request.POST.get('action') == 'Add':
            ins = BlogPost(title=_title, content=_content, author=request.user)
            if _category:  # Check if a category was selected
                ins.category = _category
            ins.save()

        elif request.POST.get('action') == 'Save Draft':
            ins = BlogPost(title=_title, content=_content,
                           author=request.user, draft=True)
            if _category:  # Check if a category was selected
                ins.category = _category
            ins.save()

        context = {'success': True}

    return render(request, 'BlogApplication/Add.html', context)


def showCategories(request):
    context = {'categories': BlogCategory.objects.all()}
    return render(request, 'BlogApplication/ShowCategories.html', context)


def chooseCategory(request):
    context = {'categories': BlogCategory.objects.all()}
    print(BlogCategory.objects.all())
    return render(request, 'BlogApplication/Add.html', context)


def createCompany(request):
    if request.method == 'POST':
        _name = request.POST['name']
        _manager = request.user
        ins = Company(name=_name, manager=_manager)
        ins.save()
    return render(request, 'BlogApplication/CreateCompany.html')


def addCategory(request):
    context = {'success': False}

    if request.method == 'POST':
        _name = request.POST['name']
        _description = request.POST['description']

        if request.POST.get('action') == 'Add':
            ins = BlogCategory(author=request.user,
                               name=_name, description=_description)
            ins.save()

        context = {'success': True}

    return render(request, 'BlogApplication/AddCategory.html', context)


def deleteCategory(request, pk):
    obj = BlogCategory.objects.get(id=pk)
    # if request.user == obj.author or request.user == request.user.is_superuser:
    obj.delete()
    return redirect("categories")


def editCategory(request, pk):

    category = BlogCategory.objects.get(id=pk)
    # if request.user == category.author or request.user == request.user.is_superuser:
    form = BlogCategoryForm(instance=category)
    if request.method == 'POST':
        form = BlogCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    context = {'form': form, 'categoryID': pk}
    return render(request, 'BlogApplication/EditCategory.html', context)
    # else:
    # return HttpResponseForbidden("You are not authorized to edit this category.")


def publishPost(request, pk):

    post = BlogPost.objects.get(id=pk)
    post.draft = False
    post.save()
    return redirect('posts')


def addComment(request, pk):
    post = BlogPost.objects.get(id=pk)
    comments = Comment.objects.filter(blogPostID=post)
    if request.method == 'POST':
        _content = request.POST['content']
        ins = Comment(content=_content, author=request.user, blogPostID=post)
        ins.save()
    return render(request, 'BlogApplication/Details.html', {'post': post, 'comments': comments})


def postDetails(request, pk):
    post = BlogPost.objects.get(id=pk)
    comments = Comment.objects.filter(blogPostID=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'BlogApplication/Details.html', context)
