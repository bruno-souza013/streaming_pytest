def pode_assistir(idade, premium):
    if premium:
        return True
    if idade >= 18:
        return True
    return False

def pode_baixar(premium):
    return premium

def qualidade_video(premium):
    if premium:
        return "HD"
    return "HD"