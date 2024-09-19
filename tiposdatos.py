print("Clases V2 jireh correa")
# Zona de clase 
class Datos :
    #El constructor funcion
    def __init__(self,estatura, peso):
        self.estatura= estatura
        self.peso= peso
    def mostrarDatos(self):
        print(f"estatura: {self.estatura}  mts,  peso  {self.peso}kg: ")
    def mi_lista(self):
        celulares= ["Samsung", "ipod", "chafa"]
        print(celulares)
        for cel in celulares:
            print(cel)
    #tuplas
    def animal_tupla(self):
        perros = ("solovino", "negro", "guero")
        for uncom in perros:
            print(uncom) 
    #Conjuntos
    def balones_conjunto(self):
        balones= {"molden", "spalding", "wilson"}
        for balones in balones:
            print(balones)
    #Diccionarios
    def comida_diccionario(self):
        comida =	{
        "tacos": "papitas",
        "frijoles": "flautas",
        "vence": 2026
        }
        print(comida)
        for salsa in comida:
            print(salsa)

#Creacion de objeto info
info= Datos(1.60, 60.1)

#Utilizando el objeto
info.mostrarDatos()
print("lista de marcas por jireh correa")
info.mi_lista()
info.animal_tupla()
info.balones_conjunto()
info.comida_diccionario()