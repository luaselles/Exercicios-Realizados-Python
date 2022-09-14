class Pessoa(object):
    __RG="000000000"
    __CPF="00000000000"
    def __init__(self,nomeC,RG,CPF,sexo):
        self.__nomeC = nomeC
        self.__RG = RG
        self.__CPF = CPF
        self.__sexo = sexo

    def getSobre(self):
        sobre = self.__nomeC.split(' ')
        return sobre[1:]

    def getvalidaCPF(self):
        num = len(self.__CPF)
        if num==11:
            mult = int(self.__CPF[0]) * 10
            mult1 = int(self.__CPF[1]) * 9
            mult2 = int(self.__CPF[2]) * 8
            mult3 = int(self.__CPF[3]) * 7
            mult4 = int(self.__CPF[4]) * 6
            mult5 = int(self.__CPF[5]) * 5
            mult6 = int(self.__CPF[6]) * 4
            mult7 = int(self.__CPF[7]) * 3
            mult8 = int(self.__CPF[8]) * 2
            soma=mult+mult1+mult2+mult3+mult4+mult5+mult6+mult7+mult8
            b=(soma*10)%11
            if int(self.__CPF[9])==b:
                mul = int(self.__CPF[0]) * 11
                mul1 = int(self.__CPF[1]) * 10
                mul2 = int(self.__CPF[2]) * 9
                mul3 = int(self.__CPF[3]) * 8
                mul4 = int(self.__CPF[4]) * 7
                mul5 = int(self.__CPF[5]) * 6
                mul6 = int(self.__CPF[6]) * 5
                mul7 = int(self.__CPF[7]) * 4
                mul8 = int(self.__CPF[8]) * 3
                mul9 = int(self.__CPF[9]) * 2
                somaa = mul + mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8 + mul9
                c = (somaa * 10) % 11
                if int(self.__CPF[10])==c:
                    return "CPF VALIDO"
                else:
                    return "CPF INVALIDO"
            else:
                return "CPF INVALIDO"
        else:
            return "CPF INVALIDO"

    def GetNome(self):
        return self.__nomeC

    def SetNome(self, nomeC):
        self.__nomeC = nomeC

    def GetCPF(self):
        return self.__CPF

    def SetCPF(self, CPF):
        self.__CPF = CPF

    def GetRG(self):
        return self.__RG

    def SetRG(self, RG):
        self.__RG = RG

    def Setsexo(self, sexo):
        self.__sexo = sexo

    def Getsexo(self):
        return self.__sexo


class Country(object):
    def __init__(self,paisN,POP,area):
         self.__paisN = paisN
         self.__POP = POP
         self.__area = area


    def GetpaisN(self):
        return self.__paisN

    def SetpaisN(self, paisN):
        self.__paisN = paisN

    def GetPOP(self):
        return self.__POP

    def SetPOP(self, POP):
        self.__POP = POP

    def Getarea(self):
        return self.__area

    def Setarea(self, area):
        self.__area = area

    def getPopDensity(self):
        return self.__POP / self.__area
