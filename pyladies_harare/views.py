from django.views.generic import TemplateView
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, get_user_model, logout

from datetime import datetime
from .models import Post, Meetup, Page, Contact, Category
from .forms import ContactForm, CommentForm, SignupForm
=======
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from datetime import datetime
from .models import Post, Meetup, Page, Contact, Category
from .forms import ContactForm, CommentForm
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2


def get_meetup():
    meetups = Meetup.objects.filter(fromdate=timezone.now()).order_by('-fromdate')[:5]
    return meetups
    

def get_category():
    categories = Category.objects.all()
    return categories


class HomeView(TemplateView):
    template_name = "pyladies_harare/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['posts'] = Post.objects.all().order_by('-published_date')
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class AboutView(TemplateView):
    template_name = "pyladies_harare/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About'
        context['pages'] = Page.objects.filter(slug='about')
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class MeetupsView(TemplateView):
    template_name = "pyladies_harare/meetups.html"

    def get_context_data(self, **kwargs):
        context = super(MeetupsView, self).get_context_data(**kwargs)
        context['title'] = 'Our Meetups'
        context['pages'] = Page.objects.filter(slug='meetups')
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class UpcomingView(TemplateView):
    template_name = "pyladies_harare/upcoming.html"

    def get_context_data(self, **kwargs):
        context = super(UpcomingView, self).get_context_data(**kwargs)
        context['title'] = 'Upcoming Meetups'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class PastMeetupsView(TemplateView):
    template_name = "pyladies_harare/past.html"

    def get_context_data(self, **kwargs):
        context = super(PastMeetupsView, self).get_context_data(**kwargs)
        context['title'] = 'Past Meetups'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class PostDetailView(TemplateView):
    template_name = "pyladies_harare/post_detail.html"
    comment_form = CommentForm()

    def get_context_data(self, pk, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Blog Post'
        context['categories'] = get_category()
        context['post'] = get_object_or_404(Post, pk=pk)
        context['meetups'] = get_meetup()
        context['comment_form'] = self.comment_form
        context['year'] = datetime.now().year
        return context


class ContactView(TemplateView):
    template_name = "pyladies_harare/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


<<<<<<< HEAD

class SignupView(TemplateView):
    signup_form = SignupForm
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['title'] = 'Sign Up'
=======
class LoginView(TemplateView):
    template_name = "account/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Log in'
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context

<<<<<<< HEAD
    def get(self, request):
        form = self.signup_form(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.signup_form(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaning the data on the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name, {'form': form})

    
'''

#we are usung flask built in log in.



class LoginView(TemplateView):
    template_name = "account/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Log in'
=======

class SignupView(TemplateView):
    template_name = "account/signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['title'] = 'Sign Up'
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


<<<<<<< HEAD
#using django built in log in.....l kept this in case you want to use it



=======
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2
class LogoutView(TemplateView):
    template_name = "account/logout.html"

    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data(**kwargs)
        context['title'] = 'Logged out'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
<<<<<<< HEAD
        return context     '''
=======
        return context
>>>>>>> 98cea01602e7e33d2f135a2914e9d707cba3c5a2
