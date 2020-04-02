class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def retangulo(self):
        if pow(self.c, 2) == (pow(self.a, 2) + pow(self.b, 2)):
            return True
        return False

    def semelhantes(self, triangulo):
        return self.tipo_lado() == triangulo.tipo_lado()

    def tipo_lado(self):
        if self._lados(self.a, self.b, self.c) == 3:
            return f"escaleno"
        elif self._lados(self.a, self.b, self.c) == 1:
            return f"equilátero"
        return f"isósceles"

    def _lados(self, a: int, b: int, c: int) -> int:
        lados = [a, b, c]
        return len(set(lados))
