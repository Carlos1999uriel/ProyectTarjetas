class Tarjetas():
    numTar = 0

    def setNumTar(self, num):
        self.numTar = num

    def getNumTar(self):
        return self.numTar

    def GenMos(self, num):
        i=1
        a=num
        b=1
        cad =""
        cad += "******Tarjeta "+str(self.getNumTar())+"******\n"
        for j in range (0,64):
            cad+="["+str(a)+"]"
            a=a+1
            if(b==num):
                a=a+num
                b=1
            else:
                b=b+1
            if (i == 8):
                i = 0
                cad += "\n"
            i=i+1
        return cad