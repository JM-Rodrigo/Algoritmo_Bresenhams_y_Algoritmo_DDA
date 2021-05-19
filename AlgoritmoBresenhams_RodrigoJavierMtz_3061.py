import matplotlib.pyplot as plt
#Importamos la liberia matplotlib para poder graficar
    
def Bresenham(x1, y1, x2, y2, color):
    #Se hacen las operaciones para definir dx, dy y p
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = (2*dy - dx)
    
    #Asignamos lo valores de x1, y1 a x, y respectivamente 
    x = x1
    y = y1
    
    print()
    print('Valores:')
    print()
    
    #Creamos un cliclo para ir asignando los incrementos
    while (x <= x2):
        #Dibuja la grafica con rrespecto a las coordenadas en x, y
        plt.plot(round(x),round(y), color)
        #Incremento en x
        x = x + 1
        #Condicion para saber si p es menor que cero
        if (p < 0):
            p = (p + 2 * dy)
        else:
            p = p + (2*dy) -(2*dx)
            y = y + 1
        #Condicion para imprimir los valores de x, y 
        if (x<= x2):
           print('X = ',x)
           print('Y = ',y)
           print()
    #Mostramos la grafica
    plt.show()

def main():
    x1 = int(input("Ingresa el valor para X1: "))
    y1 = int(input("Ingresa el valor para Y1: "))
    x2 = int(input("Ingresa el valor para X2: "))
    y2 = int(input("Ingresa el valor para Y2: "))
    color = "r."
        
    Bresenham(x1, y1, x2, y2, color)


if __name__ == '__main__':
    main()