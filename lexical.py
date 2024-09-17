import re

RESERVADA = "entero|decimal|booleano|cadena|si|sino|mientras|hacer|verdadero|falso"
OPERADOR = "\+|-|\*|\/|%|=|==|<|>|>=|<="
SIGNO = "\(|\)|\{|\}|\"|;"
NUMERO = r"\b\d+\b"
IDENTIFICADOR = "[a-zA-Z](?:[a-zA-Z]|\d)*"


def analyze(txt:str):
    reserved = [] 
    operator = []
    sign = []
    number = []
    identifier = []

    lines:list[str] = txt.splitlines()
    for index in range(len(lines)):
        line = lines[index]
        for r in re.finditer(RESERVADA, line):
            reserved.append((r.group(), "Palabra reservada",index, r.start(), txt.count(r.group())))
        for o in re.finditer(OPERADOR, line):
            operator.append((o.group(),"Operador", index, o.start(), txt.count(o.group())))
        for s in re.finditer(SIGNO, line):
            sign.append((s.group(), "Signo", index, s.start(), txt.count(s.group())))
        for n in re.finditer(NUMERO, line):
            number.append((n.group(), "Numero", index, n.start(), txt.count(n.group())))
        for i in re.finditer(IDENTIFICADOR, line):
            if not re.search(RESERVADA, i.group()):
                identifier.append((i.group(), "Identificador",index, i.start(), txt.count(i.group())))


    return reserved, operator, sign, number, identifier

if __name__=="__main__":
    txt = """
    entero 45 d;
    decimal tr4 booleano;
    tr4=verdadero;
    cadena = "{45} Gabriel(Gonzales)"
    si 45 == 45 {
        hacer falso
    }
    """
    tokens = analyze(txt)
    print(tokens)