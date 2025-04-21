'''
    Quarta tarea de APA - Generación de números aleatorios

    Nombre y Apellido: Núria Rodríguez Pardo

    Este documento consiste en crear números aleatorios a partir del método LGC, que permite generar secuencias pseudoaleatorias de características controladas.
    Nos basamos en la siguiente expresión: x = (a * x + c) % m.

    Dónde a, c y m son parámetros que se pueden ajustar para obtener diferentes resultados, pero por defecto, 
    utilizaremos los valores del estàndar POSIX con semilla x0 = 1212121.

    TEST: 

    - Para la clase Aleat:

    -- Comprobación del funcionamiento de Aleat

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15

    -- Comprobación del reinicio de Aleat

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1

    - Para la función aleat():

    -- Comprobación del funcionamiento de aleat()

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44

    -- Comprobación del reinicio de aleat()

    >>> rand.send(24)
    38

    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
'''
class Aleat:
    '''
        Esta es una clase que representa un generador de números aleatorios. 
        Utiliza el algoritmo de generación de números aleatorios de LCG.
        Utilizamos: self.x = (self.a * self.x + self.c) % self.m (LCG). Por defecto, utilizaremos los valores del estàndar POSIX con semilla x0 = 1212121.
        
        TEST: 

        -- Comprobación del funcionamiento de Aleat

        >>> rand = Aleat(m=32, a=9, c=13, x0=11)
        >>> for _ in range(4):
        ...     print(next(rand))
        16
        29
        18
        15

        -- Comprobación del reinicio de Aleat

        >>> rand(29)
        >>> for _ in range(4):
        ...     print(next(rand))
        18
        15
        20
        1
    '''
    def __init__(self, *, m=2**31, a=1103515245, c=12345, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0
    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    def __call__(self, nuevaX):
        self.x = nuevaX

def aleat(*, m=2**31, a=1103515245, c=12345, x0=1212121):
    '''
        Esta es una funcion que representa un generador de números aleatorios. 
        Utiliza el algoritmo de generación de números aleatorios de LCG. 
        Utilizamos: x = (a * x + c) % m. Por defecto, utilizaremos los valores del estàndar POSIX con semilla x0 = 1212121.
        
        TEST: 

        -- Comprobación del funcionamiento de aleat()

        >>> rand = aleat(m=64, a=5, c=46, x0=36)
        >>> for _ in range(4):
        ...     print(next(rand))
        34
        24
        38
        44

        -- Comprobación del reinicio de aleat()

        >>> rand.send(24)
        38

        >>> for _ in range(4):
        ...     print(next(rand))
        44
        10
        32
        14
    '''
    x = x0
    while True:
        x = (a * x + c) % m  
        nuevo = yield x      # Devolver número generado
        if nuevo is not None:
            x = nuevo        # Reiniciar con nueva semilla

if __name__ == "__main__":
    import doctest
    doctest.testmod()