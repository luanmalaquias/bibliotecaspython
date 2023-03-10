from main import *

assert verifyPasswordIntergity("TEste1234") == True
assert verifyPasswordIntergity("TEste", False) == True
assert verifyPasswordIntergity("TESTE", False, False) == True
assert verifyPasswordIntergity("teste", False, True, False) == True
assert verifyPasswordIntergity("teste1234", True, True, False) == True
assert verifyPasswordIntergity("TESTE1234", True, False, True) == True

assert unmask(target = "000.000.000-00", chars = '.-') == "00000000000"
assert unmask(target = 11111111111, chars = '') == "11111111111"
assert unmask(target = "(00) 0 0000-0000", chars = '() -') == "00000000000"

assert cpfIsValid(cpf="254.648.550-41") == True
assert cpfIsValid(cpf="792.039.210-10") == True
assert cpfIsValid(cpf="348.802.540-37") == True