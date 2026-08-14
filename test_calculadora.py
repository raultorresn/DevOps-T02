import pytest

from calculadora import calcular_total


def test_total_sem_desconto():
    itens = [(10.0, 2), (5.0, 1)]

    assert calcular_total(itens) == 25.0


def test_total_com_dez_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=10) == 225.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], desconto_percentual=110)


def test_cupom_soma_ao_desconto_existente():
    itens = [(100.0, 1)]

    assert calcular_total(itens, desconto_percentual=5, cupom="DEVOPS10") == 85.0


def test_cupom_em_minusculas_funciona_normalmente():
    itens = [(100.0, 1)]

    assert calcular_total(itens, cupom="boasvindas") == 95.0


def test_cupom_nao_definido_e_invalido_e_nao_aplica_desconto():
    with pytest.raises(ValueError, match="Cupom inv"):
        calcular_total([(100.0, 1)], cupom="INEXISTENTE")

    assert calcular_total([(100.0, 1)]) == 100.0