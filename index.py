#-> Precisamos criar as classes empresa e produto -- feito 
# -> Fazer o calculo das empresas -- feito 
# -> CUSTO = VALOR FIXO + (PESO * DISTÂNCIA * VALOR KM/KG) -- feito 
#-> Conseguimos criar objetos  -- feito 
# -> conseguimos ligar -- feito 
# -> conseguimos inserir valores terminados ou indeterminados -- feito 
# -> Listar os valores do menos para o maior atraves das somas algoritmo que faz isso 
# -> criar a interface 
# -> conseguir colocar mais de 1 produto para calcular
class Produto :
    def __init__(self, nome,distance,peso ):
        self.nome = nome
        self.distance = distance 
        self.peso = peso


produto2 = Produto(input(),float(input()),float(input())) 


class Empresa :
    def __init__(self,nome,valorFixo, valorKm ):
        self.nome = nome
        self.valorFixo = valorFixo
        self.valorKm = valorKm
    def calculo(self) :
        custo = self.valorFixo + float((produto2.peso * produto2.distance * self.valorKm))
        print(custo)

    def exibir(self) :
        print(self.nome, self.valorFixo, self.valorKm)
        
    def __gt__(self) :
        pass
    def __lt__(self):
       pass 


list = []
list.append(Empresa("TransBoa até 5" ,2.10, 1.10))
list.append(Empresa("BoaDex", 10, 0.12))
list.append(Empresa("TransBoa +5" ,10, 0.01))
list.append(Empresa("BoaLog" ,4.30, 0.12))

for obj in list:
    obj.calculo()
    obj.exibir()    
    obj.__gt__()
    obj.__lt__()  
