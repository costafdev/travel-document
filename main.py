from pessoa import Pessoa
from base.paises import paises

print("=+=" * 30 + "\n" + "=+=" * 30 + "\n" + "=-=" * 30)
print(("GERADOR DE MRZ".rjust(48, "-")).ljust(90, "-"))
print("-=-" * 30 + "\n" + "---" * 30)
print("PASSPORT".rjust(45).ljust(90) + "\n")
print(("Sobrenome:".rjust(35) + "Numero do passaporte:".rjust(45)).ljust(90))
print("-" * 20 + "Nome:".rjust(10))
print("|" + "|".rjust(19) + "Nacionalidade:".rjust(19))
print("|" + "|".rjust(19) + "Nascimento:".rjust(16))
print("|" + "|".rjust(19) + "Sexo:".rjust(10))
print("|" + "|".rjust(19) + "Expira:".rjust(12))
print("|" + "|".rjust(19) + "\n" + "|" + "|".rjust(19) + "\n" + "|" + "|".rjust(19) + "\n" + "-" * 20 + "\n\n")
print("<" * 44 + "\n" + "<" * 44 + "\n\n")
print("-" * 90)

titular = Pessoa()
nacionalidade = input("Digite a opçao de pais desejada: \n [1] PORTUGAL\n [2] ESPANHA\n [3] ITALIA\n [4] BELGICA\n")
if nacionalidade == "1":
    titular.nacionalidade = paises["Portugal"]
if nacionalidade == "2":
    titular.nacionalidade = paises["Spain"]
if nacionalidade == "3":
    titular.nacionalidade = paises["Italy"]
if nacionalidade == "4":
    titular.nacionalidade = paises["Belgium"]
if nacionalidade == "5":
    titular.nacionalidade = paises["Brazil"]
titular.codepais = titular.nacionalidade
print(titular.codepais)
titular.sobrenome = input("Digite o sobrenome: ").replace(" ", "<")
titular.nome = input("Digite o primeiro nome: ")
titular.nascimento = input("Data de nascimento formato YYMMDD (note: sem espaços ou caracteres especiais; apenas os dois ùltimos digitos do ano): ")
titular.sexo = input("Sexo (M ou F): ")
titular.numdoc = input("Numero do passaporte (note: entrada de letras e numeros sem espaços ou  caracteres especiais): ")
titular.expiracao = input("Data de Expiraçao formato YYMMDD (note: sem espaços ou caracteres especiais; apenas os dois ultimos digitos do ano): \n")

print("PASSAPORTE".rjust(45, "-").ljust(90, "-"))
print(titular.codeMrzPassport())
print("IDENTIDADE".rjust(45, "-").ljust(90, "-"))
print(titular.codeMrzId())