# Definición de la clase
class gene():
    #Atributos de la clase:
    secuencia = ""
    tipo = ""
    ubicacion = "" 

    # Métodos de la clase:
    def __init__(self, secuencia, tipo, ubicacion):
        self.secuencia = secuencia
        self.tipo = tipo
        self.ubicacion = ubicacion
    # Método para evaluar el nivel de expresión del gen
    def nivelexpr(self, nivel):
        if nivel <= 0:
            print("El gen de tipo", self.tipo, "ubicado en", self.ubicacion, " no está siendo expresado.")
        else:
            print("El gen de tipo", self.tipo, "ubicado en", self.ubicacion, " está siendo expresado.")
    # Método para obtener la longitud de la secuencia del gen
    def longitud_secuencia(self):
        return len(self.secuencia)
    
# Ejemplo de uso de la clase
gene1= gene("AAACCCGGTTTATATA", "NO CODIFICANTE", "CROMOSOMA 5")
# Evaluar el nivel de expresión del gen
gene1.nivelexpr(0)
# Devolver la longitud de la secuencia del gen
print("La longitud de la secuencia del gen es:", gene1.longitud_secuencia())
