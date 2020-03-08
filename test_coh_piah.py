import unittest
from coh_piah import calcula_assinatura


class CalculaAssinaturaTestCase(unittest.TestCase):
    def test_calcula_assinatura_modelo(self):
        texto = (
            "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, "
            "há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de "
            "148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas "
            "formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham "
            "que relógios digitais são uma grande ideia."
        )
        self.assertEqual(
            calcula_assinatura(texto),
            [
                5.571428571428571,
                0.8253968253968254,
                0.6984126984126984,
                210.0,
                4.5,
                45.888888888888886,
            ],
        )
