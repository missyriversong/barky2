# intermediary, boundary between api and db
#api, no business logic; instead metaclasses with abstract methods better to deal with api endpts
#db 

#viewsets to repo...?
from .views import BookmarkViewSet, UserViewSet, SnippetViewSet
from repository import AbstractRepository

#add a layer between them?

#create and add bookmarkview, userview, and snippetview?

