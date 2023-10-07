class Fraccion:
    #constructor
    def __init__(self, numerador, denominador):
        #atributos a instacia
        self.numerador = numerador
        self.denominador = denominador
    #metodos instancia
    def imprime_fraccion(self):
        print(f"{self.numerador}/{self.denominador}")
        
        #Como sumar fracciones?
    def suma_fraccion(self, fraccion_a_sumar):
        num_resultante = self.numerador + fraccion_a_sumar.denominador + fraccion_a_sumar.numerador * self.denominador
        den_resultante = self.denominador * fraccion_a_sumar.denominador
        nueva_fraccion = Fraccion(num_resultante, den_resultante)
        return nueva_fraccion


fraccion1 = Fraccion(2, 3)
fraccion2 = Fraccion(1, 2)
fraccion3 = Fraccion(3, 7)
    #creando objeto
fraccion1.imprime_fraccion()
fraccion2.imprime_fraccion()
fraccion3.imprime_fraccion()

resultado = fraccion1.suma_fraccion(fraccion2)
resultado.imprime_fraccion()
