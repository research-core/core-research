# Generated by Django 2.2.4 on 2019-08-03 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0002_auto_20190803_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('journal_id', models.AutoField(primary_key=True, serialize=False)),
                ('journal_name', models.CharField(max_length=250, verbose_name='Name')),
                ('journal_publisher', models.CharField(blank=True, max_length=80, null=True, verbose_name='Publisher')),
                ('journal_abbreve', models.CharField(max_length=80, verbose_name='Short name')),
                ('journal_issn', models.CharField(blank=True, max_length=15, null=True, verbose_name='ISSN')),
                ('journal_essn', models.CharField(blank=True, max_length=15, null=True, verbose_name='ESSN')),
            ],
            options={
                'verbose_name': 'Research Journal',
                'verbose_name_plural': 'Research Journals',
                'ordering': ['journal_name'],
            },
        ),
        migrations.CreateModel(
            name='PubType',
            fields=[
                ('pubtype_id', models.AutoField(primary_key=True, serialize=False)),
                ('pubtype_name', models.CharField(max_length=200, verbose_name='Type name')),
            ],
            options={
                'verbose_name': 'Publication type',
                'verbose_name_plural': 'Publications - Types',
                'ordering': ['pubtype_name'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication_keypub', models.NullBooleanField(verbose_name='Is a key publication?')),
                ('publication_active', models.NullBooleanField(help_text='Uncheck this box, if you do not want to turn this publication info public.', verbose_name='Sync to website?')),
                ('publication_year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Year')),
                ('publication_received', models.DateField(blank=True, null=True, verbose_name='Received date')),
                ('publication_accepted', models.DateField(blank=True, null=True, verbose_name='Accepted date')),
                ('publication_publish', models.DateField(blank=True, null=True, verbose_name='Publish date')),
                ('publication_citations', models.CharField(blank=True, max_length=255, null=True, verbose_name='Citations')),
                ('publication_pmid', models.IntegerField(blank=True, null=True, verbose_name='Pubmed id')),
                ('publication_volume', models.CharField(blank=True, max_length=30, null=True, verbose_name='Volume')),
                ('publication_issue', models.CharField(blank=True, max_length=30, null=True, verbose_name='Issue')),
                ('publication_pages', models.CharField(blank=True, max_length=30, null=True, verbose_name='Pages')),
                ('publication_title', models.CharField(max_length=255, verbose_name='Title')),
                ('publication_abstract', models.TextField(blank=True, default='', null=True, verbose_name='Abstract')),
                ('publication_web', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('publication_authors', models.TextField(help_text="Write here the authors of the publication. Authors name's should be separated by ','", verbose_name='Authors')),
                ('publication_doi', models.CharField(blank=True, max_length=50, null=True, verbose_name='DOI')),
                ('publication_editors', models.CharField(blank=True, max_length=100, null=True, verbose_name='Editors')),
                ('publication_company', models.CharField(blank=True, max_length=100, null=True, verbose_name='Publishing company')),
                ('publication_book', models.CharField(blank=True, max_length=255, null=True, verbose_name='Book title')),
                ('publication_file', models.FileField(blank=True, null=True, upload_to='uploads/publication/publication_file', verbose_name='File')),
                ('publication_verified', models.NullBooleanField(default=False, verbose_name='This publication was verified by the staff.')),
                ('authors', models.ManyToManyField(help_text='Select the CNP Authors of this publication.', to='people.Person', verbose_name='CNP Authors')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.Journal')),
                ('pubtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.PubType')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
                'permissions': (('app_access_imp_pub', 'Access [Import publications] app'),),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=200, verbose_name='Project')),
                ('project_desc', models.TextField(default='', verbose_name='Description')),
                ('project_collaborators', models.CharField(blank=True, max_length=200, null=True, verbose_name='Collaborators')),
                ('project_funding', models.CharField(blank=True, max_length=200, null=True, verbose_name='Funding')),
                ('project_order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
                ('project_active', models.NullBooleanField(verbose_name='Active')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Groups - Projects',
                'ordering': ['project_name'],
            },
        ),
        migrations.CreateModel(
            name='JournalImpactFactor',
            fields=[
                ('journalif_id', models.AutoField(primary_key=True, serialize=False)),
                ('journalif_year', models.IntegerField(verbose_name='Year')),
                ('journalif_value', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Impact factor value')),
                ('jornal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.Journal')),
            ],
            options={
                'verbose_name': 'Journal Impact Factor',
                'verbose_name_plural': 'Journals Impact Factors',
                'ordering': ['journalif_year'],
            },
        ),
        migrations.CreateModel(
            name='JournalAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Alias')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Alias')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person')),
            ],
        ),
    ]