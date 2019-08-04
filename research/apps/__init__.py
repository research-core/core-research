from confapp import conf
from . import settings
conf += settings

from .researchgroups            import ResearchGroupsListWidget
from .journals.journals_list    import JournalListWidget
from .reports.publications      import PublicationsReports
from .publications.publications import PublicationsListWidget
from .publications.import_pubs  import ImportPublications
from .publications.authors_alias import AuthorsAliasListWidget