from scipy.io import wavfile 
import sounddevice as sd
import os
import numpy as np
import matplotlib.pyplot as plt

print("Current Working Directory:", os.getcwd())

def main():
    [fs, data] = wavfile.read("drumloop.wav")
    sd.play(data, fs*2)
    status = sd.wait() 
    apresentar_info("drumloop.wav",fs,data)
    visualizacaoGrafica2(data,fs,0,1)


def apresentar_info(fileName, fs, nrBitsQuant):
    print("Informaçao do ficheiro")
    print("Nome:" + fileName)
    print(f"Taxa de amostragem:{fs/1000}kHz")
    print(f"Quantização: {nrBitsQuant.itemsize*8} Bits")

[fs, data] = wavfile.read("drumloop.wav")    

#apresentar_info("drumloop.wav", fs, data)

print (1/data.itemsize)

def visualizacaoGrafica(*args):
    if len(args) < 2 or len(args) > 4:
        print("Invalid number of arguments. Please provide 2 to 4 arguments: (data, fs, tini, tfim)")
        return

    data = args[0]
    fs = args[1]

    nbits = data.itemsize * 8
    dataN = data / (2**(nbits-1))
    [ns, nc] = data.shape
    dur = ns / fs

    if len(args) == 2:
        tini = 0
        tfim = dur
    elif len(args) == 3:
        tini = args[2]
        tfim = dur
    elif len(args) == 4:
        tini = args[2]
        tfim = args[3]

    start_idx = int(tini * fs)
    end_idx = int(tfim * fs)
    dataNA = np.arange(tini, tfim, 1/fs)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.xlabel("Tempo[s]")
    plt.ylabel("Amplitude [-1,1]")
    plt.title("Canal Direito")
    plt.plot(dataNA[:end_idx-start_idx], dataN[start_idx:end_idx, 0])

    plt.xlabel("Tempo[s]")
    plt.ylabel("Amplitude [-1,1]")
    plt.subplot(2, 1, 2)
    plt.title("Canal Esquerdo")
    plt.plot(dataNA[:end_idx-start_idx], dataN[start_idx:end_idx, 1])
    plt.subplots_adjust(hspace=0.5)
    plt.show()

def visualizacaoGrafica2(*args):
    if len(args) < 2 or len(args) > 4:
        print("Invalid number of arguments. Please provide 2 to 4 arguments: (data, fs, tini, tfim)")
        return

    data = args[0]
    fs = args[1]    

    nbits = data.itemsize * 8
    dataN = data / (2**(nbits-1))
    [ns, nc] = data.shape
    dur = ns / fs

    if len(args) == 2:
        tini = 0
        tfim = dur
    elif len(args) == 3:
        tini = args[2]
        tfim = dur
    elif len(args) == 4:
        tini = args[2]
        tfim = args[3]


    dataNA = np.arange(tini, tfim, 1/fs)

    plt.plot(data[:,0])
    plt.axis(f"{tini} {tfim} -1 1")
    plt.show()






    
    
 
#apresente o sinal de áudio num gráfico 2D (amplitude Vs tempo)

if __name__ ==  "__main__":
    main()