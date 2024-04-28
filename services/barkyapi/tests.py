from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase
#test views....?
#https://www.django-rest-framework.org/api-guide/testing/
from .models import Bookmark, Snippet, User  #hwy no user? how to access it...?
from .views import BookmarkViewSet, UserViewSet, SnippetViewSet

# Create your tests here.
# test plan


class BookmarkTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        #https://docs.djangoproject.com/en/5.0/topics/testing/advanced/
        #
        self.bookmark = Bookmark.objects.create(
            id=1,
            title="Awesome Django",
            url="https://awesomedjango.org/",
            notes="Best place on the web for Django.",
        )
        # print(f"bookmark id: {self.bookmark.id}")
        #why idsn't date added in here?

        # the simple router provides the name 'bookmark-list' for the URL pattern: https://www.django-rest-framework.org/api-guide/routers/#simplerouter
        self.list_url = reverse("barkyapi:bookmark-list")
        self.detail_url = reverse(
            "barkyapi:bookmark-detail", kwargs={"pk": self.bookmark.id}
        )

    # 1. create a bookmark
    def test_create_bookmark(self):
        """
        Ensure we can create a new bookmark object.
        """

        # the full record is required for the POST
        data = {
            "id": 99,
            "title": "Django REST framework",
            "url": "https://www.django-rest-framework.org/",
            "notes": "Best place on the web for Django REST framework.",
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Bookmark.objects.count(), 2)
        self.assertEqual(Bookmark.objects.get(id=99).title, "Django REST framework")

    # 2. list bookmarks
    def test_list_bookmarks(self):
        """
        Ensure we can list all bookmark objects.
        """
        response = self.client.get(self.list_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["results"][0]["title"], self.bookmark.title)

    # 3. retrieve a bookmark
    def test_retrieve_bookmark(self):
        """
        Ensure we can retrieve a bookmark object.
        """
        response = self.client.get(self.detail_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["title"], self.bookmark.title)

    # 4. delete a bookmark
    def test_delete_bookmark(self):
        """
        Ensure we can delete a bookmark object.
        """
        response = self.client.delete(
            reverse("barkyapi:bookmark-detail", kwargs={"pk": self.bookmark.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bookmark.objects.count(), 0)

    # 5. update a bookmark
    def test_update_bookmark(self):
        """
        Ensure we can update a bookmark object.
        """
        # the full record is required for the POST
        data = {
            "id": 99,
            "title": "Awesomer Django",
            "url": "https://awesomedjango.org/",
            "notes": "Best place on the web for Django just got better.",
        }
        response = self.client.put(
            reverse("barkyapi:bookmark-detail", kwargs={"pk": self.bookmark.id}),
            data,
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["title"], "Awesomer Django")



#https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/
# 6. create a snippet
def SnippetTests(APITestCase):
    def setup(self):
        self.factory = APIRequestFactory()
        self.snippet = Snippet.objects.create(
            id=3,
            title="example 1",
            code="json",
            linenos=True,
            language="python?",
            style="colorful",
            owner="user@example.com",    #?fk?
        )
        self.list_url = reverse("barkyapi:snippet-list")
        self.detail_url = reverse("barkyapi:snippet-detail", kwargs={'pk': self.snippet.id})

    def test_create_snippet(self):
        data = {
            "id": 4,
            "title": "example 2",
            "code": "json",
            "linenos": True,
            "language": "python",
            "style": "colorful",
            "owner": "user@example.com",    #?fk?
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Snippet.objects.count(),2)
        self.assertEqual(Snippet.get(id=4).title, "example 2")
# 7. retrieve a snippet
    def test_retrieve_snippet(self):
        response = self.client.get(self.detail_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["title"], self.snippet.title)


# 8. delete a snippet
    def test_delete_snippet(self):
        response = self.client.delete(
            reverse("barkyapi:snippet-detail", kwargs={"pk": self.snippet.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bookmark.objects.count(), 0)
# 9. list snippets
    def test_list_snippet(self):
        # companies = [CompanyFactory() for i in range(0, 3)]?  can we use this instead of setting up instance...? 
        response = self.client.get(self.list_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["results"][0]["title"], self.bookmark.title)

# 10. update a snippet
    def test_update_snippet(self):
        data = {
            "id": 4,
            "title": "example 3",
            "code": "json",
            "linenos": True,
            "language": "python",
            "style": "friendly",
            "owner": "user@example.com",    #?fk?
        }
        response = self.client.put(
            reverse("barkyapi:snippet-detail", kwargs={"pk": self.snippet.id}),
            data,
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["title"], "example 3")

# 16. highlight a snippet
#https://pygments.org/docs/styles/
#https://www.deepanseeralan.com/tech/syntax-highlighting-code-in-python-using-pygments/
    def test_highlight(self):
        self.save(
            lexer="python",
            linenos=True,
            options="example 2",
        )
    #Not sure?  assert status.is_success...or higlighted = lexer=lexer, linenos=linesos, options=options?
    


# 11. create a user
# 12. retrieve a user
# 13. delete a user
# 14. list users
# 15. update a user

#https://stackoverflow.com/questions/71876542/while-testing-a-django-drf-application-how-can-i-make-the-user-in-my-tests-supe

def UserTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            id=2,
            username='user@example.com',
        )
        self.list_url = reverse("barkyapi:user-list")   #api-auth/
        self.detail_url = reverse(
            "barkyapi:user-detail", kwargs={"pk": self.user.id}
        )

    def test_create_user(self):
        data = {
            "id": 3,
            "username": "user3@example.com"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Bookmark.objects.count(), 2)  #only 2 right... initial setup data and this one?
        self.assertEqual(Bookmark.objects.get(id=3).username, "user3@example.com")

 
# 17. list bookmarks by user
# 20. list bookmarks by date
# 23. list bookmarks by title
# 26. list bookmarks by url

def List_By_Tests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.bookmark6 = Bookmark.objects.create(
            id=6,
            title="Title 6",
            url="title6.com",
            notes="great read",
            # date_added = datetime.date(2023, 12, 1)  ?not sure...
        )
        self.bookmark7 = Bookmark.objects.create(
            id=7,
            title="Title 7",
            url="title7.com",
            notes="great read",
        )
        self.list_by_date_url = reverse(
            "barkyapi:bookmark-by-date", kwargs={"date_added": self.bookmark.date_added}
        )

        self.list_by_title_url = reverse(
            "barkyapi:bookmark-by-title", kwargs={"title": self.bookmark.title}
        )

        self.user6 = User.objects.create(
            id=6,
            username='user6@example.com',
        )
        self.user7 = User.objects.create(
            id=7,
            username='user7@example.com',
        )

    #not sure, don't see users as fk on bookmark...?  
        self.list_by_user_url = reverse(
            "barkyapi:bookmark-by-user", kwargs={"user": self.bookmark.user.id}
        )

    

# 18. list snippets by user
# 21. list snippets by date
# 24. list snippets by title
# 27. list snippets by url