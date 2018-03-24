from django.db import models
from django.db.models import Q


def error_decorator(func):
    def wrapped():
        try:
            return func()
        except:
            return {'success': False,
                    'error': 'blablabla'}
    return wrapped


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    @staticmethod
    def recursively_insert(input_obj, parent=None):
        name = input_obj['name']
        children = input_obj.get('children')

        new_one = Category(name=name, parent=parent)
        new_one.save()

        if children:
            for child in children:
                Category.recursively_insert(child, new_one)
        return {'success': True}

    @staticmethod
    def check_unique_name(input_obj):
        set_all_names = Category._get_all_names(input_obj)
        if Category.objects.filter(name__in=list(set_all_names)):
            return True
        return False

    @staticmethod
    def _get_all_names(input_obj, set_name=None):
        if not set_name:
            set_name = set()
        set_name.add(input_obj['name'])

        if input_obj.get('children'):
            for child in input_obj.get('children'):
                Category._get_all_names(child, set_name)
        return set_name

    @staticmethod
    def get_info(id):
        response = {}
        selected = Category.objects.get(id=id)
        if selected:
            response.update({
                'id': selected.id,
                'name': selected.name
            })

            parent = selected.parent
            if parent:
                response.update({
                    'parent': {
                        'name': parent.name,
                        'id': parent.id
                    },
                })
                sublings = Category.objects.filter(parent_id=selected.parent_id).filter(~Q(id=selected.id))
                sublings = sublings
                response.update({
                    'sublings': [
                        {'name': subling.name,
                         'id': subling.id}
                        for subling in sublings
                        ]
                })
            return response