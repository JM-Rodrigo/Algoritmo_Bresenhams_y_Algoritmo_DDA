import matplotlib.pyplot as plt
#Importamos la liberia matplotlib para poder graficar
    
def DDA(x1, y1, x2, y2, color):
    #Se hacen las operaciones para definir dx, dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = 0
    
    #Se hacen las comparaciones para saber cual es mayor
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
    #Se optinen los incrementos para x, y
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    #Redondeamos los incrementos
    xInc = round(xInc,1)
    yInc = round(yInc,1)

    #Se crea un ciclo para ir asignando los incrementos 
    for i in range(0, int(steps + 1)):
        #Dibuja la grafica con rrespecto a las coordenadas en x1, y1
        plt.plot(round(x1),round(y1), color)
        #Hace el incremento
        x1 += xInc
        y1 += yInc
        
        #Imprimimos los valores de x, y para cada caso
        print('X =',x1)
        print('Y = ',y1)
    #Mostramos la grafica
    plt.show()
    
    #Imprimimos los demas valores de DDA
    print()
    print("Valores:")
    print("dx = ",dx)
    print("dy = ",dy)
    print("steps = ",steps)
    print("Xinc = ",xInc)
    print("Yinc",yInc)

def main():
    x1 = int(input("Ingresa el valor para X1: "))
    y1 = int(input("Ingresa el valor para Y1: "))
    x2 = int(input("Ingresa el valor para X2: "))
    y2 = int(input("Ingresa el valor para Y2: "))
    color = "b."
    
    DDA(x1, y1, x2, y2, color)

if __name__ == '__main__':
    main()
    
