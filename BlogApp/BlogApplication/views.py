from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib.auth.models import User
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from . forms import *
# Create your views here.

def loginView(request):
	form = AuthenticationForm()
	if request.method == "POST":
        # Get Prepared Django Login Form and fill it with user's data coming from POST request
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

	return render(request, "BlogApplication/LoginPage.html", context={"form":form})

def index(request):
    context = {'posts': BlogPost.objects.all()}
    return render(request, 'BlogApplication/Home.html', context)

def renderAdd(request):
    return render(request, 'BlogApplication/Add.html')

# class Edit(LoginRequiredMixin, UpdateView):
#     model = BlogPost
#     template_name = 'BlogApplication/Edit.html'
#     fields = ['title', 'content']
#     success_url = reverse_lazy('posts')

#     def get_queryset(self):
#         user_model = get_user_model()
#         queryset = self.model.objects.filter(author=self.request.user)
#         # print(queryset)  # Check the queryset in the console
#         return queryset

def editPost(request, pk):
    # Retrieve the Posts to be updated from the database using its primary key (pk)
    post = BlogPost.objects.get(id=pk)
    # Initialize a BlogPost instance with the existing Blog data
    form = BlogPostForm(instance=post)
    # If The form is submitted
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'postID': pk}
    return render(request, 'BlogApplication/Edit.html', context)

def deletePost(request, pk):
        obj = BlogPost.objects.get(id=pk)
        obj.delete()
        return redirect("posts")

#     # if request.user.is_authenticated:
#     #     user = request.user
#     # Get the referenced user based on user_id

def addPost(request):
    context = {'success' : False}
    if request.method =='POST':
        _title = request.POST['title']
        _content = request.POST['content']
        ins = BlogPost(title=_title, content=_content, author = request.user)
        ins.save()
        context = {'success' : True}
    return render(request, 'BlogApplication/Add.html',context)


# class Details(DetailView):
#     model = BlogPost
#     template_name = 'BlogApplication/Details.html'

#     def get_context_data(self, **kwargs):
#         # Call the parent class's method to get the default context
#         context = super().get_context_data(**kwargs)

#         # Retrieve comments related to this blog post
#         relatedComments = Comment.objects.filter(blogPostID=self.object)

#         # Add the comments to the context
#         context['comments'] = relatedComments

#         # Return the updated context
#         return context
# def blog_post_details(request, pk):
#     # Retrieve the BlogPost object
#     blog_post = get_object_or_404(BlogPost, pk=pk)

#     # Retrieve comments related to this blog post
#     related_comments = Comment.objects.filter(blogPostID=blog_post)

#     context = {
#         'blog_post': blog_post,
#         'comments': related_comments,
#     }

#     return render(request, 'BlogApplication/Details.html', context)
def postDetails(request, pk):
    # Retrieve the specific BlogPost object by its primary key or return a 404 error if it doesn't exist
    post = BlogPost.objects.get(id=pk)
    comments = Comment.objects.filter(blogPostID = post)
    context = {'post': post,'comments': comments}
    return render(request, 'BlogApplication/Details.html', context)
