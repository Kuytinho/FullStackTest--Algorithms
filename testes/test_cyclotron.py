import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cyclotron import cyclotron

def test_cyclotron():
    # Teste para uma matriz 4x4 acelerando um elétron
    matriz = cyclotron("e", 4)
    assert matriz == [['e', 'e', 'e', 'e'], [1, 1, 1, 'e'], [1, 1, 1, 'e'], [1, 1, 1, 'e']]

    # Teste para uma matriz 4x4 acelerando um próton
    matriz = cyclotron("p", 4)
    assert matriz == [['p', 'p', 'p', 'p'], ['p', 1, 1, 'p'], ['p', 1, 'p', 'p'], ['p', 'p', 'p', 1]]

    # Teste para uma matriz 4x4 acelerando um nêutron
    matriz = cyclotron("n", 4)
    assert matriz == [['n', 'n', 'n', 'n'], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    # Teste para uma matriz 4x4 sem particulas
    matriz = cyclotron("", 4)
    assert matriz == [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

# Executa os testes
test_cyclotron()