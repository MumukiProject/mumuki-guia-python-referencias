
Recordemos que el `equal?` era un mensaje que nos decía si dos objetos son el mismo. Veamos qué pasó:

```python
otro_saludo = "buen día" # se crea la variable otro_saludo que referencia al objeto "buen día"
despedida = otro_saludo # se crea la variable despedida que, por asignarle la referencia otro_saludo, apunta al mismo objeto
```

```python
ム "buen día".equal? "buen día"
=> False
ム despedida.equal? "buen día"
=> False
```

En ambos casos el resultado fue `False`, dado que aquellos strings son objetos **distintos**, a pesar de que tengan los mismos caracteres. Cada vez que escribimos un string estamos creando un nuevo objeto. Sin embargo:

```python
ム otro_saludo.equal? otro_saludo
=> True
ム despedida.equal? otro_saludo
=> True
```

¿Por qué? ¡Simple! Ambas referencias, `otro_saludo` y `despedida`, apuntan al mismo objeto. La moraleja es que declarar una variable significa agregar una nueva referencia al objeto existente, en lugar de copiarlo:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python-referencias/master/images/saludos1.png" alt="Múltiples referencias" width="300" height="auto">

Distinto sería si hacemos:

```python
otro_saludo = "buen día"
despedida = "buen día"
```

Lo cual da como resultado este ambiente:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python-referencias/master/images/saludos2.png" alt="Múltiples referencias" width="300" height="auto">


> Veamos si se entiende: declará una lista `referencias_repetidas`, que esté conformada por tres referencias a un mismo objeto (¡el que quieras!)
