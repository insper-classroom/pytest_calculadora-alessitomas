import pytest
from matematica.Calculadora import *

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    x = 3
    y = 4
    assert 7 == soma(x,y)

@pytest.mark.op_simples
def test_sub_dois_valores_positivos():
    x = 3
    y = 4
    assert -1 == sub(x,y)

@pytest.mark.op_complexas
def test_multi_dois_valores_positivos():
    x = 3
    y = 4
    assert 12 == multiplicacao(x,y)

@pytest.mark.op_complexas
def test_divião_dois_valores_positivos():
    x = 10
    y = 5
    assert 2 == divisao(x,y) 
@pytest.mark.op_complexas
def test_divião_por_zero():
    x = 10
    y = 0
    assert np.inf == divisao(x,y) 
@pytest.mark.op_media
def test_media_lista_numeros():
    lista = [2,2,5]
    assert  3 == media_lista_valores(lista) 
@pytest.mark.op_media
def test_media_lista_vazia():
    lista = []
    assert  0 == media_lista_valores(lista) 

@pytest.mark.op_media
def test_media_lista_suja():
    lista = [3,2.5,0.5,'']
    assert  2 == media_lista_valores(lista) 
