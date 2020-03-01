from django import forms
from django.contrib.auth.models import Group, User
from mainland.models import QCollection


def collections_choices():
    query = QCollection.objects.all()
    col_list = list()
    for collection in query:
        tmp = (collection.id, collection.name)
        col_list.append(tmp)
    col_list = tuple(col_list)
    return col_list


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
        ]
        labels = {
            'name': 'Название',
        }


class GroupPermsForm(forms.ModelForm):
    collections = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                            label='Тесты',
                                            choices=collections_choices(),
                                            required=False,
                                            help_text='Выберите тесты, к которым хотите открыть доступ для группы пользователей.'
                                                      'Если нужно выбрать несколько тестов - выберите их с зажатым Ctrl.')

    class Meta:
        model = Group
        exclude = ['permissions']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'groups',
        ]
        labels = {
            'groups': ('Группы'),
        }
        help_texts = {
            'groups': ('Выберите группы, к которым должен относиться пользователь. Если нужно выбрать несколько групп - выберите их с зажатым Ctrl.')
        }