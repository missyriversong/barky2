# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html

# should we test quit? No, its behavior is self-evident and not logic dependent
def test_quit_command():
    pass

# okay, should I test the other commands?
# not really, they are tighly coupled with sqlite3 and its use in the database.py module

import pytest
import commands

from database import DatabaseManager
from commands import AddBookmarkCommand, EditBookmarkCommand, ListBookmarksCommand, DeleteBookmarkCommand, ImportGitHubStarsCommand


#test addbookmark
def testAddBookmarkCommand():
    #arrange
    db = DatabaseManager("bookmarks.db")
    data = {   
        #db?
        "title": "infinity",
        "url": "yayoi",
        "notes": "memoir",
    }
    addBookmark = AddBookmarkCommand() #what goes in here?
    #https://pynative.com/python-class-method/

    #act
    addBookmark.execute(data)  #:
        # db.update(db, data)
        #                ^
        # SyntaxError: invalid syntax
    
    #assert
    AddBookmarkCommand.assertEqual(data["title"],"infinity")



#test editbookmark     - update not found in database.py, wip
def testEditBookmarkCommand():
    #arrange
    db = DatabaseManager("bookmarks.db")
    editBookmark = EditBookmarkCommand()  
    data = {
        "title": "mirrors",
    }

    #act
    editBookmark.execute(data)   

    #assert
    editBookmark.assertEqual(data["title"],"mirrors")

#test listbookmark
def testListBookmark():
    #arrange
    db = DatabaseManager("bookmarks.db")
    listBookmark = ListBookmarksCommand("title")   #pass through?

    #act
    listBookmark.execute()

    #assert
    

#test deletebookmark

#test importgithub