#repos use ORM...can't remember book vs. lecture..supplementary materials...where i left off...need to take better notes...
import abc
from models import Bookmark, Snippet   #? User

from serializers import BookmarkSerializer, SnippetSerializer, UserSerializer

  #method that is declared, but contains no implementation. Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
  #This exception may be raised by user code to indicate that an attempted operation on an object is not supported, and is not meant to be. If an object is meant to support a given operation but has not yet provided an implementation, NotImplementedError is the proper exception to raise.
class AbstractRepository(abc.ABC): 
  @abc.abstractmethod
  def add(self, model):   #create using generic model?  and then insert later upon concrete instantiation .....for each specific model later???
    raise NotImplementedError

  @abc.abstractmethod
  def get(self, model):   #get specific?   
    raise NotImplementedError
  
  #update
  #delete for each bookmark, snippet, user?  foreign key?

  @abc.abstractmethod
  def update(self, model):
    raise NotImplementedError

  @abc.abstractmethod
  def delete(self, model):  
    raise NotImplementedError


#why isn't list part of this? but in the instance of SQLRepo?
#what is snippet?


# class SQLRepository(AbstractRepository):
#   def add(self, bookmark):
#     self.add(bookmark)

#   def get(self, reference):
#     return self.query(models.Bookmark).filter(reference=reference).one()
  
#   def list(self):
#     return self.query(models.Bookmark).all()

  # def update(self, request, pk=None):



#? 
class BookmarkRepository(AbstractRepository):
  
  def add(self, data):
    serializer_class = BookmarkSerializer(data=data)   #where did i find this?
  
  def get(self):
    return BookmarkSerializer

  def update(self, data):
    #https://www.geeksforgeeks.org/update-a-dictionary-in-python-using-for-loop/
    #not sure
      for key, value in data.items():
        data[key] = value

  def delete(self, pk, data):   #?
    if pk == pk:
      for key, value in data.items():
        del key[value]
 


class SnippetRepository(AbstractRepository):
  
  def add(self, data):
    serializer_class =  SnippetSerializer(data=data)   #where did i find this?
  
  def get(self):
    return SnippetSerializer

  def update(self, data):
    #https://www.geeksforgeeks.org/update-a-dictionary-in-python-using-for-loop/
    #not sure
      for key, value in data.items():
        data[key] = value

  def delete(self, pk, data):   #?
    if pk == pk:
      for key, value in data.items():
        del key[value]



class UserRepository(AbstractRepository):
  
  def add(self, data):
    serializer_class = UserSerializer(data=data)   #where did i find this?
  
  def get(self):
    return UserSerializer

  def update(self, data):
    #https://www.geeksforgeeks.org/update-a-dictionary-in-python-using-for-loop/
    #not sure
      for key, value in data.items():
        data[key] = value

  def delete(self, pk, data):   #?
    if pk == pk:
      for key, value in data.items():
        del key[value] 