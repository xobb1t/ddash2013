from django.template import Library
from ..forms import UserEditForm

register = Library()


@register.inclusion_tag('accounts/tags/user_edit_form.html',
                        takes_context=True)
def user_edit_form(context):
    user = context.get('user')
    return {
        'form': UserEditForm(instance=user),
        'user': user
    }
