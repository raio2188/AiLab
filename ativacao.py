def ReLU(x):
    return max(x, 0)

def Derivada_ReLU(x):
    return 1 if x > 0 else 0

def Leaky_ReLU(x):
    return x if x > 0 else 0.1 * x

def Derivada_Leaky_ReLU(x):
    return 1 if x > 0 else 0.1

def Identidade(x):
    return x

def Derivada_Identidade(x):
    return 1