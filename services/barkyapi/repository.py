#repos use ORM
import abc
import model

  #method that is declared, but contains no implementation. Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
class AbstractRepository(abc.ABC): 
  @abc.abstractmethod
  def add(self, bookmark: model.Bookmark):


