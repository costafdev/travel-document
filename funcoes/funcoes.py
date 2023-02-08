from string import ascii_uppercase, digits

def calcHash(string: str) -> str:
    """funcao que calcula o hash de uma string (hash
    dos dados do titular do documento
    """

    alfanum = digits + ascii_uppercase  #variavel com caracteres alfanumericos
    string = string.upper().replace("<", "0")
    peso = [7, 3, 1]   #usado no calculo da hash
    soma = 0           #soma ponderada

    for i in range(len(string)):
        c = string[i]   #cada caractere da string
        if c not in alfanum:   #verif se o caractere eh alfanum
            raise ValueError("%s contem caracteres invalidos" % string, c)   #forca o erro
        soma += alfanum.index(c) * peso[i%3]    #o calculo da       a soma ponderada
    return str(soma%10)                         #  da hash          o quociente euclidiano

