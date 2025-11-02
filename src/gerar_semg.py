import numpy as np 
import matplotlib.pyplot as plt 
import scipy.signal as signal

def gerar_semg_simulado():
    t = np.linspace(0, 1, 1000) # 1 segundo, 1kHz
    # Sinal base + ruido
    semg = np.random.normal(0, 0.1, 1000) * np.sin(2*np.pi*50*t)
    return t, semg

t, sinal = gerar_semg_simulado()
plt.plot(t, sinal)
plt.title('Meu Primeiro Sinal sEMG')
plt.show()