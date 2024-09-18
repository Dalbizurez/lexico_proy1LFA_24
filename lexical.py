import re

RESERVADA = "entero|decimal|booleano|cadena|si|sino|mientras|hacer|verdadero|falso"
OPERADOR = "\+|-|\*|\/|%|=|==|<|>|>=|<="
SIGNO = "\(|\)|\{|\}|\"|;"
NUMERO = r"\b\d+\b"
IDENTIFICADOR = "[a-zA-Z](?:[a-zA-Z]|\d)*"

def lexycalAnalysis(txt:str):
    pattern = r"(?P<reserved>entero|decimal|booleano|cadena|si|sino|mientras|hacer|verdadero|falso)|(?P<operator>\+|-|\*|\/|%|==|=|<|>|>=|<=)|(?P<sign>\(|\)|\{|\}|\"|;)|(?P<number>\b\d+\b)|(?P<id>[a-zA-Z](?:[a-zA-Z]|\d)*)"
    matches = []
    errors = []
    lines = txt.splitlines()
    for l in range(len(lines)):
        line = lines[l]
        errorLine = line
        for match in re.finditer(pattern=pattern, string=line):
            matches.append((match.group(), match.lastgroup, l+1, match.start()+1, txt.count(match.group())))
            errorLine = errorLine.replace(match.group(), "")
        if len(errorLine.strip()) != 0:
            errors.append((line, l+1))
    return errors if errors else matches


def analyze(txt:str):
    reserved = [] 
    operator = []
    sign = []
    number = []
    identifier = []
    errors = []
    errorTxt = txt

    lines:list[str] = txt.splitlines()
    errorLines:list[str] = errorTxt.splitlines()
    for index in range(len(lines)):
        line = lines[index]
        errorLine = errorLines[index]
        for r in re.finditer(RESERVADA, line):
            reserved.append((r.group(), "Palabra reservada",index+1, r.start(), txt.count(r.group())))
            errorLine = errorLine.replace(r.group(),"")
        for o in re.finditer(OPERADOR, line):
            operator.append((o.group(),"Operador", index+1, o.start(), txt.count(o.group())))
            errorLine = errorLine.replace(o.group(),"")
        for s in re.finditer(SIGNO, line):
            sign.append((s.group(), "Signo", index+1, s.start(), txt.count(s.group())))
            errorLine = errorLine.replace(s.group(),"")
        for n in re.finditer(NUMERO, line):
            number.append((n.group(), "Numero", index+1, n.start(), txt.count(n.group())))
            errorLine = errorLine.replace(n.group(),"")
        for i in re.finditer(IDENTIFICADOR, line):
            if not re.search(RESERVADA, i.group()):
                identifier.append((i.group(), "Identificador",index+1, i.start(), txt.count(i.group())))
            errorLine = errorLine.replace(i.group(),"")
        if len(errorLine.strip()) != 0:
            errors.append((line, index+1))
    
    return errors, reserved, operator, sign, number, identifier

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
    print(lexycalAnalysis(txt))