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

#####Posts
def index(request):
    companies = Company.objects.all()  # Retrieve all companies
    company_users_dict = {}
    for company in companies:
        users_for_company = User.objects.filter(company=company)
        company_users_dict[company] = users_for_company
    context = {'posts': BlogPost.objects.all(), 'company_users_dict': company_users_dict}
    return render(request, 'BlogApplication/Home.html', context)


def addPost(request):
    context = {'success': False}
    categories = BlogCategory.objects.all()  # Get all available categories

    if request.method == 'POST':
        form = BlogPostForm(request.POST)

        if form.is_valid():
            _title = form.cleaned_data['title']
            _content = form.cleaned_data['content']
            _category_ids = request.POST.getlist('category')  # Get selected category IDs

            if request.POST.get('action') == 'Add':
                ins = BlogPost(title=_title, content=_content, author=request.user)
            elif request.POST.get('action') == 'Save Draft':
                ins = BlogPost(title=_title, content=_content, author=request.user, draft=True)
            
            ins.save()
            ins.category.set(_category_ids)  # Use set() to assign categories

            context = {'success': True, 'categories': categories}

    else:
        form = BlogPostForm()  # Create a new form instance for rendering

    context['form'] = form  # Include the form in the context
    context['categories'] = categories

    return render(request, 'BlogApplication/Add.html', context)


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
    # return HttpResponseForbidden("You are not authorized to delete this post.")


def postDetails(request, pk):
    post = BlogPost.objects.get(id=pk)
    comments = Comment.objects.filter(blogPostID=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'BlogApplication/Details.html', context)


def publishPost(request, pk):

    post = BlogPost.objects.get(id=pk)
    post.draft = False
    post.save()
    return redirect('posts')

#####Categories
def showCategories(request):
    companies = Company.objects.all()  # Retrieve all companies
    company_users_dict = {}
    for company in companies:
        users_for_company = User.objects.filter(company=company)
        company_users_dict[company] = users_for_company
    context = {'categories': BlogCategory.objects.all(), 'company_users_dict': company_users_dict}
    return render(request, 'BlogApplication/ShowCategories.html', context)


def chooseCategory(request):
    context = {'categories': BlogCategory.objects.all()}
    print(BlogCategory.objects.all())
    return render(request, 'BlogApplication/Add.html', context)


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

#####Comments
def addComment(request, pk):
    post = BlogPost.objects.get(id=pk)
    comments = Comment.objects.filter(blogPostID=post)
    if request.method == 'POST':
        _content = request.POST['content']
        ins = Comment(content=_content, author=request.user, blogPostID=post)
        ins.save()
    return render(request, 'BlogApplication/Details.html', {'post': post, 'comments': comments})

#####Companies
def createCompany(request):
    if request.method == 'POST':
        _name = request.POST['name']
        _manager = request.user
        ins = Company(name=_name, manager=_manager)
        ins.save()
    return render(request, 'BlogApplication/CreateCompany.html')


def showCompanies(request):
    context = {'companies': Company.objects.all()}
    return render(request, 'BlogApplication/Companies.html', context)


def companyDetails(request, pk):
    company = Company.objects.get(id=pk)
    writers = User.objects.filter(company=company)
    context = {'company': company, 'writers': writers}
    return render(request, 'BlogApplication/CompanyDetails.html', context)