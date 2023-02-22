from main import *

assert verifyPasswordIntergity("TEste1234") == True
assert verifyPasswordIntergity("TEste", False) == True
assert verifyPasswordIntergity("TESTE", False, False) == True
assert verifyPasswordIntergity("teste", False, True, False) == True
assert verifyPasswordIntergity("teste1234", True, True, False) == True
assert verifyPasswordIntergity("TESTE1234", True, False, True) == True