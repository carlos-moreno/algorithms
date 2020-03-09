import unittest
from coh_piah import calcula_assinatura, calcula_type_token


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


class CalculaTypeTokenTestCase(unittest.TestCase):
    def test_type_token_0_743(self):
        texto = (
            "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção "
            "do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, "
            "coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o "
            "prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona "
            "quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe "
            "transparência."
        )
        self.assertEqual(calcula_type_token(texto), 0.743)

    def test_type_token_0_777(self):
        texto = (
            "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar "
            "um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser "
            "poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que "
            "se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a "
            "hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma "
            "noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, "
            "tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem "
            "suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
        )
        self.assertEqual(calcula_type_token(texto), 0.777)
