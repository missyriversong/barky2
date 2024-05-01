from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from barkyapi.models import Bookmark
from barkyarch.domain.model import DomainBookmark
from barkyarch.services.commands import (
    AddBookmarkCommand,
    ListBookmarksCommand,
    DeleteBookmarkCommand,
    EditBookmarkCommand,
)


class TestCommands(TestCase):
    def setUp(self):
        right_now = localtime().date()

        self.domain_bookmark_1 = DomainBookmark(
            id=1,
            title="Test Bookmark",
            url="http://www.example.com",
            notes="Test notes",
            date_added=right_now,
        )

        self.domain_bookmark_2 = DomainBookmark(
            id=2,
            title="Test Bookmark 2",
            url="http://www.example2.com",
            notes="Test notes 2",
            date_added=right_now,
        )

        # edit takes in model object..
        # data = {
        #     "id" : 1,
        #     "title" : "Test Bookmark1",
        #     "url" : "http://www.example1.com",
        #     "notes" : "Test notes1",
        #     "date_added" : right_now,
        # }

        # another version of bookmark 1 data?
        self.domain_bookmark_1v2 = DomainBookmark(
            id=1,
            title="Test Bookmark v2",
            url="http://www.example v2.com",
            notes="Test notes v2",
            date_added=right_now,
        )

    def test_command_add(self):
        add_command = AddBookmarkCommand()
        add_command.execute(self.domain_bookmark_1)   #takes in object

        # run checks
        # one object is inserted
        self.assertEqual(Bookmark.objects.count(), 1)

        # that object is the same as the one we inserted
        self.assertEqual(Bookmark.objects.get(id=1).url, self.domain_bookmark_1.url)

        add_command.execute(self.domain_bookmark_2)
        self.assertEqual(Bookmark.objects.count(), 2)
        
        

    def test_command_list(self):
        list_command = ListBookmarksCommand()
        list_command.execute()   #no data needed...?  return all bookmark objs?
        self.assertEqual(Bookmark.objects.count(), 2)   #?
        #AssertionError: 0 != 2

    def test_command_edit(self):
        edit_command = EditBookmarkCommand()   #takes in model ojbect?
        edit_command.execute(self.domain_bookmark_1v2)

        self.assertEqual(self.domain_bookmark_1v2.title, "Test Bookmark 2")
        #AttributeError: 'NoneType' object has no attribute 'save'
        #cant find something similar.in stack overflow
    
    def test_command_delete(self):
        delete_command = DeleteBookmarkCommand(self.domain_bookmark_1)   #get by url not id?...and then delete it...?
        #TypeError: DeleteBookmarkCommand() takes no arguments....self.domain_bookmark_1.url?
        delete_command.execute()   
        self.assertEqual(Bookmark.objects.count(), 1)  
        #or verify not present url? 
        #https://docs.djangoproject.com/en/5.0/topics/testing/overview/   should it be notpresent or something..?
        #https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
        self.assertisNone(self.domain_bookmark_1)  #?


# ./manage.py test barkyarch.tests.TestCommands