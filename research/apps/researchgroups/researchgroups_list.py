from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from people.models import Group as ResearchGroup

from .researchgroups_form import ResearchGroupFormWidget


class ResearchGroupsListWidget(ModelAdminWidget):
    """
    """
    UID = 'groups'
    TITLE = 'Groups'

    MODEL = ResearchGroup

    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ICON = 'rocket'
    ORQUESTRA_MENU_ORDER = 10

    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL

    USE_DETAILS_TO_EDIT = False

    EDITFORM_CLASS = ResearchGroupFormWidget

    LIST_DISPLAY = [
        'group_name',
        'group_subject',
        'person',
        'grouptype',
        # 'groupdjango',
    ]

    LIST_FILTER = ['grouptype']

    SEARCH_FIELDS = ['group_name__icontains']

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True

        # user is allowed if Coordinator / Admin / Manager of any group
        for group in user.groups.all():
            parts = group.name.split(': ')
            if (
                len(parts) == 3 and
                parts[0] == 'PROFILE' and
                parts[1] in ('Group Coordinator',
                             'Group Admin',
                             'Group Manager')
            ):
                return True
        else:
            return False
