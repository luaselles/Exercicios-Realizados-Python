from modulo import *

#Exercicio 1#
print(("> > > Exercicio 1 < < <"))
arg=Country("Argentina",43590368,2780400)
arg.SetpaisN("Brasil")
arg.SetPOP(189970841)
arg.Setarea(8514876.59)
print("Densidade Populacional do "+arg.GetpaisN()+" é igual a "+str(arg.getPopDensity()))
print("")
print("---------------------------------------------")
print("")
#Exercicio 2#
print(("> > > Exercicio 2 < < <"))
pessoa = Pessoa("MARIA","777777777","1478855522122","Feminino")
print("Nome Completo: %s" %pessoa.GetNome())
print("RG: %s" % pessoa.GetRG())
print("CPF: %s" % pessoa.GetCPF())
print("Sexo: %s" % pessoa.Getsexo())
print("Sobrenome: %s" % pessoa.getSobre())
print(pessoa.getvalidaCPF())
