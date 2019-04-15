from django.db import models
from django.db.models import Q
from django.contrib.auth.models import Group as Dgroup
from django.utils import timezone
from common.models import Permissions

from .group_queryset import GroupQuerySet

class GroupType(models.Model):
    """
    Represents a Type of a Group in the system
    Example: Fellow, Staff
    """
    grouptype_id = models.AutoField(primary_key=True)           #: ID
    grouptype_name = models.CharField('Name', max_length=200)   #: Name

    class Meta:
        ordering = ['grouptype_name',]
        verbose_name = "Group type"
        verbose_name_plural = "Group - Types"
        app_label = 'research'

    def __str__(self):
        return self.grouptype_name






class Group(models.Model):
    """
    Represents a Group in the system
    Example: Fly Facillities, Lima
    """

    group_id = models.AutoField(primary_key=True)                   #: ID
    grouptype = models.ForeignKey(GroupType, verbose_name = 'Type', on_delete=models.CASCADE) #: Fk to the Group Type Table. e.g. staff
    group_name = models.CharField('Name', max_length=200)           #: Name
    group_subject = models.CharField('Subject', max_length=200)     #: Subject of a group
    group_web = models.URLField( verbose_name = 'Web site', blank=True, null=True)         #: URL to the Group Web site if exists
    group_people = models.ImageField('People',upload_to="uploads/group/group_people", blank=True, null=True)    #: Group People Image file to upload Button
    group_img = models.ImageField('Thumbnail',upload_to="uploads/group/group_img", blank=True, null=True)       #: Group Image file to be upload Button and a Thumbnail URL of the image
    group_desc = models.TextField('Description', default='', blank=True, null=True)                             #: Description of the Group
    members = models.ManyToManyField('humanresources.Person', verbose_name = 'Members',through='GroupMember')                    #: Persons belong to that Group (Connection to the Person Table)
    person = models.ForeignKey('humanresources.Person', related_name = 'Head', verbose_name = 'Head', blank=True, null=True, on_delete=models.CASCADE)     #: The head of that Group is a Fk to the Person Table
    groupdjango = models.ForeignKey(Dgroup, blank=True, null=True, verbose_name='Groups in Django', related_name = 'group_django', on_delete=models.CASCADE)

    objects = GroupQuerySet.as_manager()

    class Meta:
        ordering = ['group_name',]
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        app_label = 'research'

    def __str__(self):
        return self.group_name

    @staticmethod
    def autocomplete_search_fields():
        return ("group_name__icontains",)


class MemberCategory(models.Model):
    """
    Represents a Ctegory of a member in a Group
    Exmple: Collaborations, Visiting fellow
    """

    membercategory_id = models.AutoField(primary_key=True)          #: ID
    membercategory_name = models.CharField('Name', max_length=200)  #: Name

    class Meta:
        ordering = ['membercategory_name', ]
        verbose_name = "Group - Member category"
        verbose_name_plural = "Group - Members categories"
        app_label = 'research'

    def __str__(self):
        return self.membercategory_name











class GroupMemberQuerySet(models.QuerySet):

    def active(self):
        """
        Filter only active people
        """
        today = timezone.localtime(timezone.now()).date()
        query = Q()
        query.add(Q(date_joined__lte=today, date_left__gte=today), Q.OR)
        query.add(Q(date_joined__lte=today, date_left=None), Q.OR)
        query.add(Q(date_joined=None, date_left__gte=today), Q.OR)
        query.add(Q(date_joined=None, date_left=None), Q.OR)
        return self.filter(query)


class GroupMember(models.Model):
    """
    Represents a Person wich is a Member of that Group
    """

    person = models.ForeignKey('humanresources.Person', on_delete=models.CASCADE)  #: Fk to the Person table
    group = models.ForeignKey(Group, on_delete=models.CASCADE)    #: Fk to the Group table
    membercategory = models.ForeignKey(MemberCategory, verbose_name = 'Category', blank=True, null=True, on_delete=models.CASCADE) #: Fk to the member category of that Person in the Group

    date_joined = models.DateField('Joined', null=True, blank=True)
    date_left = models.DateField('Left', null=True, blank=True)

    position = models.ForeignKey(
        to='humanresources.Position',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    objects = GroupMemberQuerySet.as_manager()

    class Meta:
        db_table = "research_group_members"
        app_label = 'research'

    def __str__(self):
        position = self.membercategory or self.person.position
        return f'{self.person.name} is a {position} in {self.group}'
