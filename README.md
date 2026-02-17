El proyecto implementa el algoritmo clásico de Cifrado César, un método de cifrado por sustitución donde cada letra del texto original se desplaza un número determinado de posiciones dentro del alfabeto.

El programa permite:

°Cifrar texto

°Descifrar texto

°Elegir entre alfabeto en inglés o español (incluyendo la ñ)

°Mantener mayúsculas y minúsculas

°Conservar espacios y símbolos especiales

Este proyecto fue desarrollado como práctica de fundamentos de programación y criptografía básica.

¿Cómo funciona el algoritmo?

El Cifrado César fue utilizado por Julio César para enviar mensajes secretos.

El funcionamiento es el siguiente:

°Se define un alfabeto (inglés o español).

°Se pide al usuario:

°Si desea cifrar o descifrar.

°El idioma del alfabeto.

°El texto.

°El número de desplazamiento.

°Para cada letra:

°Se busca su posición en el alfabeto.

°Se aplica la fórmula:

nueva_posicion = (posicion + desplazamiento) % len(alfabeto)


°El operador % permite que el desplazamiento sea circular (cuando llega al final del alfabeto vuelve al inicio).

°Si el usuario elige descifrar, el desplazamiento se convierte en negativo.

Opción 1: Ejecutarlo desde la terminal (forma correcta)
 1° Tener Python instalado

Puede verificarlo con:

python --version


Si aparece algo como:

Python 3.x.x


Entonces ya lo tiene instalado.

2️° Descargar el código

Si lo subes a GitHub, puede hacer:

git clone https://github.com/iliusi21/Cifrado-Cesar/.git


O simplemente descargar el archivo .py.

3️°  Ir a la carpeta donde está el archivo

Ejemplo:

cd ejercicio cesar.py

 Ejecutarlo
python main.py


