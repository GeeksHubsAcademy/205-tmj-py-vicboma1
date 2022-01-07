<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


    Considere el siguiente problema:

    Dado el siguiente abecedario con letras estándares :
	
	abcdefghijklmnopqrstuvwxyz
	
	Se quiere calcular el número de posiciones de cada letra respecto a la última aparición de la misma en la formación 
    de una cadena indicándolo en la salida de un array con las posiciones del abecedario.

	Ejemplo:

	Input => 'abacba'
	Resultado => [6, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	Explicación:

	La letra a = 6 dado que la palabra empieza por 'a' y acaba por 'a'.
	El número de posición desde la primera aparición hasta la última son 6
	a(1),b(2),a(3),c(4),b(5),a(6)

	La letra b = 4 dado que la letra 'b' está en la segunda posición y la útima aparición en la quinta.
	b(1),a(2),c(3),b(4)
	
	La letra c = 1 dado que la letra 'c' solo aparece una vez.
	c(1)


	Los inputs de entrada se restringen de la siguiente manera :

	5 ≤ palabra.length ≤ 50

	No se contemplan otros casos.



    En la carpeta 'src/kata.py' se encuentra el fichero con 
    la definición de nuestros métodos vacíos.
    En la carpeta 'tests/kata_test.py' se encuentra el fichero 
    con la suite de test.

    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.

    [Test Suite]

    tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [  5%]
    tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [ 10%]
    tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 15%]
    tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 21%]
    tests/test_kata.py::Test_kata::test_apply_13 PASSED                      [ 26%]
    tests/test_kata.py::Test_kata::test_apply_14 PASSED                      [ 31%]
    tests/test_kata.py::Test_kata::test_apply_15 PASSED                      [ 36%]
    tests/test_kata.py::Test_kata::test_apply_16 PASSED                      [ 42%]
    tests/test_kata.py::Test_kata::test_apply_17 PASSED                      [ 47%]
    tests/test_kata.py::Test_kata::test_apply_18 PASSED                      [ 52%]
    tests/test_kata.py::Test_kata::test_apply_19 PASSED                      [ 57%]
    tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 63%]
    tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 68%]
    tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 73%]
    tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 78%]
    tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 84%]
    tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 89%]
    tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 94%]
    tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]


## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
