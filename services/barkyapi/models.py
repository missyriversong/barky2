from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
#pip install Pygments


#  generic syntax highlighter suitable for use in code hosting, forums, wikis or other applications that need to prettify source code. 


# pygments stuff - breaks down code into token aka smallest unit of meaningful code then apply relevant ..format for language and style...?
LEXERS = [item for item in get_all_lexers() if item[1]] 
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class Bookmark(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    notes = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    #? not sure how to create users...auth.User? 
    highlighted = models.TextField()

    class Meta:
        ordering = ["created"]

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} - {self.id}"
    



    #     fields = ["id", "username", "snippets"]
# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.username}"    