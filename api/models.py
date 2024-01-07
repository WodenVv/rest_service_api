from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Todos(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    comentario = models.CharField(max_length=100)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    
    
