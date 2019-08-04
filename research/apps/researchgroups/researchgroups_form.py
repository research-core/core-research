from django.conf import settings

from confapp import conf
from pyforms.basewidget import segment
from pyforms.controls import ControlImg
from pyforms_web.widgets.django import ModelFormWidget

from people.models import Person

from .memberships import MembershipsListWidget
from .projects import ProjectsListWidget


class ResearchGroupFormWidget(ModelFormWidget):

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB
    HAS_CANCEL_BTN_ON_EDIT = False
    CLOSE_ON_REMOVE = True

    READ_ONLY = (
        'grouptype',
        'person',
        'groupdjango',
    )

    INLINES = [MembershipsListWidget, ProjectsListWidget]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    FIELDSETS = [
        ('grouptype', 'person', 'groupdjango'),
        ' ',
        (
            segment(
                'h3: IDENTIFICATION',
                'group_name',
                'group_subject',
                field_css='fourteen wide',
            ),
            segment(
                '_img',
                field_style='max-width:330px;'
            )
        ),
        {
            '1:Group Information': [
                'group_desc', 'group_web', 'group_img', '_grpimg',
            ],
            '2:Projects': ['ProjectsListWidget'],
            '3:Members': ['MembershipsListWidget'],
        }
    ]

    def __init__(self, *args, **kwargs):

        self._img = ControlImg('Image', label_visible=False)
        self._grpimg = ControlImg('Image', label_visible=False)

        super().__init__(*args, **kwargs)

        self.person.changed_event = self.__update_image_evt

        self.group_img.changed_event = self.__update_group_img_evt

        self.__update_image_evt()
        self.__update_group_img_evt()

    def __update_group_img_evt(self):
        self._grpimg.value = self.group_img.value

    def __update_image_evt(self):
        try:
            person = Person.objects.get(pk=self.person.value.pk)
        except Person.DoesNotExist:
            url = Person.DEFAULT_PICTURE_URL
        else:
            url = person.thumbnail_url('300x300')
        self._img.value = url

    @property
    def title(self):
        obj = self.model_object
        if obj is None:
            return super().title.fget(self)
        else:
            return "Group: {0}".format(obj.group_name)

    @title.setter
    def title(self, value):
        super().title.fset(self, value)
