def ReLU(x):
    return max(x, 0)

def derivada_relu(x):
    return 1 if x > 0 else 0

def leaky_relu(x):
    return x if x > 0 else 0.1 * x

def derivada_leaky_relu(x):
    return 1 if x > 0 else 0.1

def Identidade(x):
    return x

def Derivada_Identidade(x):
    return 1
