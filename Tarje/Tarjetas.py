from Tarje import Interfaz
from Generador import Generador


class Preguntar:
    def __init__(self):
        obj = Interfaz.mainloop()

        obj = Generador.Tarjetas()
        suma = 0


        obj.setNumTar(1)
        obj.GenMos(1)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if(op == "s"):
            suma = suma+1

        obj.setNumTar(2)
        obj.GenMos(2)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if (op == "s"):
            suma = suma + 2

        obj.setNumTar(3)
        obj.GenMos(4)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if (op == "s"):
            suma = suma + 4

        obj.setNumTar(4)
        obj.GenMos(8)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if (op == "s"):
            suma = suma + 8

        obj.setNumTar(5)
        obj.GenMos(16)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if (op == "s"):
            suma = suma + 16

        obj.setNumTar(6)
        obj.GenMos(32)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if (op == "s"):
            suma = suma + 32

        obj.setNumTar(7)
        obj.GenMos(64)
        op = str(input("Esta tu numero en esta tarjeta? (s/n) \n"))
        if (op == "s"):
            suma = suma + 64

        print("Tu numero es: ", suma)

class main():
    mi_app = Preguntar()

if __name__ =="__main__":
    main()