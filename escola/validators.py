import re

def cpf_invalido(cpf: str) -> bool:
    return len(cpf) != 11

def nome_invalido(nome: str) -> bool:
    return not str(nome).isalpha()

def telefone(telefone: str) -> bool:
    telefone = f"{telefone[:2]} {telefone[2:7]}-{telefone[7:]}"
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    valid = re.findall(modelo, telefone)
    return not valid

def cep_invalido(cep: str) -> bool:
    cep = f"{cep[0:5]-cep[5:]}"
    modelo = "[0-9]{5}-[0-9]{3}"
    valid = re.findall(modelo, cep)
    return not valid

def rg_invalido(rg: str) -> bool:
    return len(rg) != 9
