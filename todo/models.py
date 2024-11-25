from django.db import models
class Todo(models.Model):
    """
    This class represents a Todo item in the application.#+

class Todo(models.Model):#-
    Attributes:#+
    title (CharField): The title of the Todo item.#+
    completed (BooleanField): Indicates whether the Todo item is completed.#+
    is_archived (BooleanField): Indicates whether the Todo item is archived.#+

    Methods:
    __str__(): Returns the title of the Todo item.#+
    """
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns the title of the Todo item.#+

        Returns:
        str: The title of the Todo item.#+
        """
        return self.title
