import secrets
import string

def generatePassword(safety: int) -> str:
    """Retorna uma senha gerada automaticamente de acordo com o nível de segurança"""

    alphabet = string.ascii_letters + string.digits

    if safety <= 1:
        for tentativa in range(500):
            password = ''
            for _ in range(4):
                choice = secrets.choice(alphabet)
                password += choice + choice
            if safety == 0:
                if verifyPasswordIntergity(password, upper=False):
                    break
            elif safety == 1:
                if verifyPasswordIntergity(password):
                    break

    elif safety == 2:
        password = ''
        for tentativa in range(500):
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(8))
            if verifyPasswordIntergity(password):
                break

    return password

def verifyPasswordIntergity(password: str, numeric=True, lower=True, upper=True) -> bool:
    """Verifica se a senha contém numeros e caracteres em lower case"""
    passwordIntergity = False

    passwordNumeric = False
    passwordLower = False
    passwordUpper = False

    for letter in password:
        if letter.isnumeric():
            passwordNumeric = True if not passwordNumeric else True
        if letter.islower():
            passwordLower = True if not passwordLower else True
        if letter.isupper():
            passwordUpper = True if not passwordUpper else True

    if passwordNumeric == numeric and passwordLower == lower and passwordUpper == upper:
        passwordIntergity = True

    return passwordIntergity

def unmask(target: any, chars: str) -> str:
    """Remove todos os caracteres que forem passados no parametro chars"""
    if type(target) != str:
        target = str(target)
    for char in chars:
        target = target.replace(char, '')
    return target

def cpfIsValid(cpf: str|int) -> bool:
    """Verifica se o CPF é valido"""
    if type(cpf) == int:
        cpf = str(cpf)

    cpf = unmask(cpf, '.-')

    if len(cpf) != 11:
        return False
    
    primeiros9 = cpf[:9]
    verificadores = cpf[9:]
    
    def _calcPrimeiroDigito(primeiros9):
        result = 0
        primeiros9Invert = primeiros9[::-1]
        for index,number in enumerate(primeiros9Invert):
            result += (index+2) * int(number)
    
        resto = result % 11
        if resto < 2:
            primeiroDigito = 0
        else:
            primeiroDigito = 11 - resto
        
        return primeiroDigito
    
    def _calcSegundoDigito(primeiros9, primeiroDigito):
        result = 0
        primeiros9 = primeiros9 + str(primeiroDigito)
        primeiros9Invert = primeiros9[::-1]
        for index,number in enumerate(primeiros9Invert):
            result += (index+2) * int(number)
        
        resto = result % 11
        if resto < 2:
            segundoDigito = 0
        else:
            segundoDigito = 11 - resto
        
        return segundoDigito

    primeiroDigito = _calcPrimeiroDigito(primeiros9)
    segundoDigito = _calcSegundoDigito(primeiros9, primeiroDigito)
    
    if primeiroDigito == int(verificadores[0]) and segundoDigito == int(verificadores[1]):
        return True
    
    return False
