- Abrir la carpeta Lección 17 - Proyecto en Pycharm
# Clase Question
## Atributos:
- text (sera el texto de la pregunta) **CREADO AL INSTANCIAR LA CLASE**
- answer (sera la respuesta correcta a la pregunta) **CREADO AL INSTANCIAR LA CLASE**
## RETO 1
- Crear la Clase Question.
### Solución:
```
# question_model.py
class Question:  
    def __init__(self, text, answer):  
        self.text = text  
        self.answer = answer
```
# Crear el question_bank
- Crear un arreglo llamado `question_bank` que contenga objetos de la clase **Question** con los datos del arreglo de `question_data` del archivo de *data.py*.
### Solucion:
```
# main.py  
from question_model import Question  
from data import question_data  
  
question_bank = []  
for question in question_data:  
    q_text = question['text']  
    q_answer = question['answer']  
  
    new_question = Question(text=q_text, answer=q_answer)  
  
    question_bank.append(new_question)
```

- **Versión optimizada**
```
# main.py
from question_model import Question  
from data import question_data  
  
question_bank = []  
for question in question_data:  
    question_bank.append(Question(text=question['text'], answer=question['answer']))
```
# Clase QuizBrain
```
 # TODO1: Hacer las preguntas al usuario.
 # TODO2: Checar si la respuesta del usuario es correcta.
 # TODO3: Checar si es la ultima pregunta del quiz.
```
## Atributos:
`question_number`: 
- Su valor por defecto es *0*.
- Cambiara según el numero de pregunta que se haya preguntado.

`questions_list`:
- Tendrá que ser dado al instanciar la clase.
- Contendrá la lista con los preguntas de la clase **Question**.
## Metodos:
`next_question`:
- Tendrá que mostrar la pregunta al usuario dependiendo `question_number`.
## Reto
- Crear la clase de QuizBrain con sus atributos.
### Solucion:
```
# quiz_brain.py  
class QuizBrain:  
    def __init__(self, question_list):  
        self.question_number = 0  
        self.question_list = question_list
```
## Reto
- Crear el metodo `next_question()`.
- Que debe mostrar la pregunta asignada al `self.question_number` en el siguiente formato:
![[Pasted image 20240305100031.png]]
### Solucion:
```
# quiz_brain.py  
class QuizBrain:  
    def __init__(self, question_list):  
        self.question_number = 0  
        self.question_list = question_list  
  
    def next_question(self):  
        current_question = self.question_list[self.question_number] # Retorna un objeto de clase Question.  
        self.question_number += 1   
user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?:')
```
## Reto: Crear metodo still_has_questions().
- Crear una funcion llamada `still_has_questions()` que cheque si aun quedan preguntas en `self.question_list`.
- La funcion tiene retornar un boolean.
- **Consejo:** usar while loop.
### Solucion:
```
def next_question(self):  
    current_question = self.question_list[self.question_number] # Retorna un objeto de clase Question.  
    self.question_number += 1  
    user_answer = input(f'Q.{self.question_number}: {current_question.text} (T/F)?: ').lower()
```
Versión optimizada:
```
def still_has_questions(self):  
    return self.question_number < len(self.question_list)
```
Implementación en *main.py*:
```
# main.py  
from question_model import Question  
from data import question_data  
from quiz_brain import QuizBrain  
  
# ------------ CREACION DEL QUESTION BANK ------------ #  
question_bank = []  
for question in question_data:  
    q_text = question['text']  
    q_answer = question['answer']  
  
    new_question = Question(text=q_text, answer=q_answer)  
  
    question_bank.append(new_question)  
  
# ------------ MAIN ------------ #  
quiz = QuizBrain(question_list=question_bank)  
  
while quiz.still_has_questions():  
    quiz.next_question()  
  
print('Quiz terminado')
```
## Reto: Checar la respuesta del usuario
- Agregar un atributo `score` e inicializarlo en 0.
- Crear la clase `check_answer()` que se encargara de checar si la respuesta del usuario es o no es la correcta.
	- En caso de ser correcta imprimir en consola que es la respuesta correcta.
	- En caso de estar equivocado imprimir en consola que es la respuesta incorrecta y mostrar la respuesta correcta.
	- Al final mostrar cuantas preguntas ha tenido bien del total. *Ejemplo: 5/8*
### Solucion:
```
def check_answer(self, user_answer, correct_answer):  
    if user_answer.lower() == correct_answer.lower():  
        self.score += 1  
        print('You got it right!')  
    else:  
        print("That's wrong!")  
        print(f'The correct answer is: {correct_answer}')  
  
    print(f'Your current score is: {self.score}/{self.question_number}.\n')
```
Integración:
```
def next_question(self):  
    current_question = self.question_list[self.question_number] # Retorna un objeto de clase Question.  
    self.question_number += 1  
    user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ').lower()  
  
    self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)
```
