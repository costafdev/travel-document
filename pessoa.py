from funcoes.funcoes import calcHash


class Pessoa:
    def __init__(self):
        self.sobrenome = ""
        self.nome = ""
        self.codepais = ""
        self.numdoc = ""
        self.nacionalidade = ""
        self.nascimento = ""
        self.sexo = ""
        self.expiracao = ""

    #@getters
    def getcodepais(self):
        return self.codepais
    def getsobrenome(self):
        return self.sobrenome
    def getnome(self):
        return self.nome
    def getnumdoc(self):
        return self.numdoc
    def getnacionalidade(self):
        return self.nacionalidade
    def getnascimento(self):
        return self.nascimento
    def getsexo(self):
        return self.sexo
    def getexpiracao(self):
        return self.expiracao

    def linha1Passport(self):
        return ("P<"+self.codepais.upper().ljust(3, "<")+(self.sobrenome+"<<"+self.nome).upper().ljust(39, "<"))
    def linha2Passport(self):
        opcional = "<" * 14
        return (self.numdoc.upper().ljust(9, "<") +
                calcHash(self.numdoc) +
                self.nacionalidade.upper().ljust(3, "<") +
                self.nascimento+calcHash(self.nascimento) +
                self.sexo.upper() +
                self.expiracao +
                calcHash(self.expiracao) +
                opcional +
                calcHash(opcional) +
                calcHash(self.numdoc.ljust(9, "<").replace("<", "0") +
                         calcHash(self.numdoc) +
                         self.nascimento +
                         calcHash(self.nascimento) +
                         self.expiracao +
                         calcHash(self.expiracao) +
                         opcional +
                         calcHash(opcional)))

    def codeMrzPassport(self):
        return (self.linha1Passport() + "\n" + self.linha2Passport())
    ######## IDENTIDADE #########
    def linha1Id(self):
        opcional = "<" * 15
        return ("I<" +
                self.codepais.upper().ljust(3, "<") +
                self.numdoc.ljust(9, "<") +
                calcHash(self.numdoc) +
                opcional)
    def linha2Id(self):
        opcional = "<" * 11
        return (self.nascimento +
                calcHash(self.nascimento) +
                self.sexo +
                self.expiracao +
                calcHash(self.expiracao) +
                self.nacionalidade +
                opcional +
                calcHash(self.numdoc +
                         calcHash(self.numdoc) +
                         self.nascimento +
                         calcHash(self.nascimento) +
                         self.expiracao +
                         calcHash(self.expiracao)+
                         opcional +
                         calcHash(opcional)))
    def linha3Id(self):
        return (self.sobrenome+"<<"+self.nome).ljust(30, "<")

    def codeMrzId(self):
        return (self.linha1Id()+"\n"+self.linha2Id()+"\n"+self.linha3Id()).upper()