# intermediary, boundary between api and db
#api, no business logic; instead metaclasses with abstract methods better to deal with api endpts
#db 

#viewsets to repo...?
from .views import BookmarkViewSet, UserViewSet, SnippetViewSet
from repository import AbstractRepository

#add a layer between them?

#get bookmarkview, userview, and snippetview?

#https://breadcrumbscollector.tech/how-to-implement-a-service-layer-in-django-rest-framework/
#only logic of application or domain...?
#model Order vs. def confirm
#UI, restful....application logic...db

#https://emcarrio.medium.com/business-logic-in-a-django-project-a25abc64718c
#?BookmarkManager to retrieve and edit them?

#? services as a class, function...creating a bookmark or getting list of bookmarks?




#https://www.madelyneriksen.com/blog/service-pattern-in-django
#why aren't we making a service to create bookmarks and users?  or does a serliazers really serve as a service handler?

#need to move on from this..look at holistic code and thenn come back and fill in understanding...