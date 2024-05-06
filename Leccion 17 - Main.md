# Como crear una clase:
```
class User:
 pass

user_1 = User()
```
- Explicar como usar `pass`.
- Explicar que es PascalCase. 
  
---
# Agregar atributos a una clase:
- Se pueden agregar atributos de la siguiente manera:
	- `user_1.id = '001'`
	- `user_1.username = 'Dante Kaled'`
- Explicar el *constructor* de una clase.
- Repaso de que son los atributos.
```
class User:  
    # La funcion init se ejecuta siempre que se cree un objeto.  
    def __init__(self, user_id, username):  
        self.id = user_id  
        self.username = username  
  
  
user_1 = User(user_id='001', username="Dante Kaled")
```
- Explicar que no todos los atributos tienen que ser seteados al instanciar la clase.
```        
# Explicar el self.followers  
self.followers = 0  
```

---
# Crear metodos:
- Todos los metodos de una clase siempre tienen que contener el atributo *self*.
```
class User:  
    # La funcion init se ejecuta siempre que se cree un objeto.  
    def __init__(self, user_id, username):  
        self.id = user_id  
        self.username = username  
        self.followers = 0  
        self.following = 0  
  
    def follow(self, user):  
        user.followers += 1  
        self.following += 1  
  
  
user_1 = User(user_id='001', username="Dante Kaled")  
user_2 = User(user_id='002', username='Christian')  
  
user_1.follow(user_2)
```
