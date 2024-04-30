from typing import Set
import abc
from barkyarch.domain.model import DomainBookmark
from barkyapi.models import Bookmark


class AbstractRepository(abc.ABC):
    """
    Because it is based on an ABC, this abstract class repository can be used with
    any data storage strategy.
    """

    def __init__(self):
        self.bookmarks_set = set()  # type: Set[DomainBookmark]

    def add(self, bookmark: DomainBookmark):
        self.bookmarks_set.add(bookmark)

    def get(self, id) -> DomainBookmark:
        bookmark = self._get(id)
        if bookmark:
            self.bookmarks_set.add(bookmark)
        return bookmark

    @abc.abstractmethod
    def _get(self, id):
        raise NotImplementedError

#shouldn't put and delete be here...?
    def put(self, id):  #what about the extra data?
        pass
    #first _get(id)
    #

    def delete(self, id):
        pass
    #.delete(bookmark)?

class DjangoRepository(AbstractRepository):
    """
    This concrete instance of the repository uses the Django ORM as the data storage strategy.
    """

    def add(self, bookmark):
        super().add(bookmark)
        self.update(bookmark)

    def update(self, bookmark):
        Bookmark.update_from_domain(bookmark)
        #if update is in add...what is it doing here....?

    def _get(self, id):
        return Bookmark.objects.filter(id=id).first().to_domain()

    def put(self, data):  #no attribute
        bookmark = Bookmark.objects.get(pk=DomainBookmark.id)
        bookmark.title = data.title
        bookmark.url = data.url
        bookmark.notes = data.notes

    # def update_from_domain(batch: domain_model.Batch):
    #     try:
    #         b = Batch.objects.get(reference=batch.reference)  #(1)
    #     except Batch.DoesNotExist:
    #         b = Batch(reference=batch.reference)  #(1)
    #     b.sku = batch.sku
    #     b.qty = batch._purchased_quantity
    #     b.eta = batch.eta  #(2)
    #     b.save()
    #     b.allocation_set.set(
    #         Allocation.from_domain(l, b)  #(3)
    #         for l in batch._allocations
    #     )

    def list(self):
        return [bookmark.to_domain() for bookmark in Bookmark.objects.all()]
#https://dev.to/manukanne/a-python-implementation-of-the-unit-of-work-and-repository-design-pattern-using-sqlmodel-3mb5
    def delete(self, id):
        return Bookmark.objects.filter(id=id).delete()    #nope error...ughh filter or exclude?

#not using?  confused...
class DjangoApiRepository(AbstractRepository):
    """
    This concrete instance of the repository uses the DRF, which abstracts its own data storage
    strategy.
    """

    def add(self, bookmark):
        # super().add(bookmark)
        # self.update(bookmark)
        pass

    def update(self, bookmark):
        # django_models.Bookmark.update_from_domain(bookmark)
        pass

    def _get(self, id):
        # return (
        #     django_models.Bookmark.objects.filter(id=id)
        #     .first()
        #     .to_domain()
        # )
        pass

    def list(self):
        # return [bookmark.to_domain() for bookmark in django_models.Bookmark.objects.all()]
        pass
