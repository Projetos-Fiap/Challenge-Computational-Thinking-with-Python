from math import sqrt
from math import pow

qtdEcopontos = 0
coordsEcopontos = []
i = 0 
coordCasa = ()

# Lê quantos ecopontos vamos cadastrar
qtdEcoPontos  = float(input("Entre com a quantidade de Ecopontos que deseja cadastrar:\n"))

# Cadastra as coordenadas dos ecopontos
while i < qtdEcoPontos:
    x = float(input("Entre com a coordenada X do %d° ecoponto:\n" % (i+1)))
    y = float(input("Entre com a coordenada Y do %d° ecoponto:\n" % (i+1)))
    coordsEcopontos += [(x,y)]
    i += 1

# Cadastra as coordenadas da casa do usuário
x = float(input("Entre com a coordenada X da sua casa: \n"))
y = float(input("Entre com a coordenada Y da sua casa: \n"))
coordCasa = (x,y)

# Percorre todos os ecopontos e calcula a distancia entre cada um deles e a casa do usuário
menorDistancia = float('inf')
ecopontoMaisProximo = ()
for coordEcoponto in coordsEcopontos:
    #Calcula distancia entre a casa e o ponto atual
    #Usando teorema de pitágoras (distancia = sqrt(A^2 + Y^2))
    # Onde A é a diferença entre a coordenada X do ecoponto e da casa
    # e B é a diferença entre a coordenada X do ecoponto e da casa
    
    distancia = sqrt(pow(coordEcoponto[0]-coordCasa[0],2) + pow(coordEcoponto[1] - coordCasa[1], 2))
    # Checa se a distancia entre a casa do usuário e o ecoponto atual 
    # é menor do que todas encontradas até agora
    if distancia < menorDistancia:
        menorDistancia = distancia
        ecopontoMaisProximo = coordEcoponto

print(ecopontoMaisProximo)
print(menorDistancia)
print("O ecoponto mais próximo é o das coordenadas (", ecopontoMaisProximo[0], ", ", ecopontoMaisProximo[1], ")\n")






