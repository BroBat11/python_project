# Import necessary modules from Django
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Product, Category
from .serializers import bibloSerializer
from .forms import *
from .utils import *

# Define a menu for the site
menu = ["about", "Log In", "Categories"]

# Define views for handling web requests and API endpoints

# View for displaying the home page with a list of published products
class ProductHome(DataMixin, ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'posts'

    # Override get_context_data to add custom context data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    # Override get_queryset to filter only published products
    def get_queryset(self):
        return Product.objects.filter(is_published=True)

# View for adding a new product (requires login)
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    # Override get_context_data to add custom context data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))

# View for user registration
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    # Override get_context_data to add custom context data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

# View for handling contact form submissions
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = reverse_lazy('home')

    # Override get_context_data to add custom context data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    # Override form_valid to print form data and redirect to home
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

# View for user login
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    # Override get_context_data to add custom context data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    # Override get_success_url to redirect to home after login
    def get_success_url(self):
        return reverse_lazy('home')

# View for user logout
def logout_user(request):
    logout(request)
    return redirect('login')

# View for displaying an about page with paginated product list
def about(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})

# View for displaying details of a specific product
class ShowPost(DataMixin, DetailView):
    model = Product
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    # Override get_context_data to add custom context data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

# View for displaying products in a specific category
def show_category(request, cat_id):
    posts = Product.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'main/index.html', context=context)

# Custom error handler views for HTTP status codes 400, 403, 404, and 500
def handler400(request, exception):
    return render(request, "400.html", status=400)

def handler403(request, exception):
    return (render(request, "403.html", status=403))

def handler404(request, exception):
    return (render(request, "404.html", status=404))

def handler500(request):
    return (render(request, "500.html", status=500))

# Custom pagination class for the API
class bibloAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2

# API view for listing and creating products
class bibloAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = bibloSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = bibloAPIListPagination

# API view for updating a product
class bibloAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = bibloSerializer
    permission_classes = (IsAuthenticated, )

# API view for destroying (deleting) a product
class bibloAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = bibloSerializer
    permission_classes = (IsAdminOrReadOnly, )
