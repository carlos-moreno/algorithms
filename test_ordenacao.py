import ordenacao
import pytest


class TestOrdenador:
    @pytest.fixture
    def o(self):
        return ordenacao.Ordenacao(100)

    @pytest.fixture
    def lista_quase_ordenada(self):
        c = ordenacao.Ordenacao(100)
        return c.list_generation_v2()

    @pytest.fixture
    def lista_aleatoria(self):
        c = ordenacao.Ordenacao(100)
        return c.list_generation()

    def esta_ordenada(self, lst):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True

    def test_bolha_curta_quase_ordenada(self, o, lista_quase_ordenada):
        o.bubblesort_v2(lista_quase_ordenada)
        assert self.esta_ordenada(lista_quase_ordenada)

    def test_selecao_direta_quase_ordenada(self, o, lista_quase_ordenada):
        o.direct_selection(lista_quase_ordenada)
        assert self.esta_ordenada(lista_quase_ordenada)

    def test_bolha_curta_aleatoria(self, o, lista_aleatoria):
        o.bubblesort_v2(lista_aleatoria)
        assert self.esta_ordenada(lista_aleatoria)

    def test_selecao_direta(self, o, lista_aleatoria):
        o.direct_selection(lista_aleatoria)
        assert self.esta_ordenada(lista_aleatoria)
