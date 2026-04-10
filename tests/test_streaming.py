import pytest
from app.streaming import pode_assistir, pode_baixar, qualidade_video

def test_usuario_menor_sem_premium():
    assert pode_assistir(15, False) == False

def test_usuario_adulto_sem_premium():
    assert pode_assistir(20, False) == True

def test_usuario_premium():
    assert pode_assistir(10, True) == True

def test_download_premium():
    assert pode_baixar(True) == True

def test_download_nao_premium():
    assert pode_baixar(False) == False

def test_qualidade():
    assert qualidade_video(True) == "4K"