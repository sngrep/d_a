from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


class UserView(ListView):
    model = User
    paginate_by = 10
    template_name = 'administration/user_list.html'


class GroupView(ListView):
    model = Group
    paginate_by = 10
