from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generin import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


class UserView(ListView):
    model = User
    queryset = User.objects.all()
    paginate_by = 10


class GroupView(ListView):
    model = Group
    paginate_by = 10
