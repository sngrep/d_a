from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from mainland.models import QCollection
from .forms import GroupForm, UserForm, GroupPermsForm
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView
                                  )
from guardian.shortcuts import get_objects_for_user, get_objects_for_group, assign_perm, remove_perm


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'administration/group_create_view.html'
    success_url = reverse_lazy('administration:group_list')


class AdminView(TemplateView):
    template_name = 'administration/admin_view.html'


class UserView(ListView):
    model = User
    paginate_by = 10
    template_name = 'administration/user_list.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'administration/user_update_view.html'
    form_class = UserForm
    success_url = reverse_lazy('administration:user_list')


class GroupView(ListView):
    model = Group
    paginate_by = 10
    template_name = 'administration/group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_perm_dict = dict()
        for group in context['group_list']:
            group_perm_dict[group] = get_objects_for_group(group, 'view_quiz', QCollection)
        context['group_perms'] = group_perm_dict
        context['group_list'] = QCollection.objects.all()
        print(context)
        return context


# class GroupPermissionView(UpdateView):
#     model = Group
#     template_name = 'administration/group_perms.html'
#     form_class = GroupPermsForm
#     success_url = reverse_lazy('administration:group_list')
#
#     def form_valid(self, form):
#         group = self.request.POST['name']
#         collection_list = self.request.POST.getlist('collections')
#         # print(group)
#         # print(collection_list)
#         # assign_perm()
#         # print(self.request.POST)
#         return super().form_valid(form)


def give_permission(request, **kwargs):
    print(kwargs)
    group = Group.objects.get(id=kwargs['group'])
    quiz = QCollection.objects.get(id=kwargs['quiz'])
    print(f"Group = {group.name}")
    print(f"Quiz = {quiz.name}")
    assign_perm('view_quiz', group, quiz)
    return redirect("administration:group_list")


def remove_permission(request, **kwargs):
    print(kwargs)
    group = Group.objects.get(id=kwargs['group'])
    quiz = QCollection.objects.get(id=kwargs['quiz'])
    print(f"Group = {group.name}")
    print(f"Quiz = {quiz.name}")
    remove_perm('view_quiz', group, quiz)
    return redirect("administration:group_list")