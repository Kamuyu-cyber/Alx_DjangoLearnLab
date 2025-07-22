from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)  # Ensure max_length is set
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)  # Ensure max_length is set
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Ensure related_name
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)  # Ensure max_length is set
    books = models.ManyToManyField(Book, related_name='libraries')  # Ensure related_name
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Ensure max_length is set
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')  # Ensure related_name
    
    def __str__(self):
        return self.name
