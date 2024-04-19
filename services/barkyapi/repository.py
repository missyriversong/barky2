#repos use ORM...can't remember book vs. lecture..supplementary materials...where i left off...need to take better notes...
import abc
import models

  #method that is declared, but contains no implementation. Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
  #This exception may be raised by user code to indicate that an attempted operation on an object is not supported, and is not meant to be. If an object is meant to support a given operation but has not yet provided an implementation, NotImplementedError is the proper exception to raise.
class AbstractRepository(abc.ABC): 
  @abc.abstractmethod
  def add(self, bookmark: models.Bookmark):   #create
    raise NotImplementedError

  @abc.abstractmethod
  def get(self, reference) -> models.Bookmark:   #get specific?   
    raise NotImplementedError

#why isn't list part of this? but in the instance of SQLRepo?


class SQLRepository(AbstractRepository):
  def add(self, bookmark):
    self.add(bookmark)

  def get(self, reference):
    return self.query(models.Bookmark).filter(reference=reference).one()
  
  def list(self):
    return self.query(models.Bookmark).all()
