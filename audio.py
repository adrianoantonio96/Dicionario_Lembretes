import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
import struct


def main(args):
    

    chunk = 1024
    formato = pyaudio.paInt16
    canais = 1
    taxaDeAmostragem = 44100
    tempoDeGravacao = 5
    nomeArquivoSaida = "saidaMic.wav"
    nomeArquivoSaidaFiltrado= "saidaMicFiltrado.wav"
    

    deltaX= 1.0/taxaDeAmostragem
    
    objetoPyAudio = pyaudio.PyAudio()

    print ("Gravando durante " , tempoDeGravacao ,"  segundos...")

    streamMic = objetoPyAudio.open(format=formato,channels=canais, rate=taxaDeAmostragem, input=True, frames_per_buffer=chunk)

    

    framesWav = []


    for nLoop in range(0, int(taxaDeAmostragem / chunk * tempoDeGravacao)):
            dadosLidosMic = streamMic.read(chunk)
            framesWav.append(dadosLidosMic)

    streamMic.stop_stream()
    streamMic.close()
    objetoPyAudio.terminate()
    
    framesWavJuntos= b''.join(framesWav)
    
    wavDataList =  [struct.unpack("&amp;amp;lt;h", framesWavJuntos[nLoop] + framesWavJuntos[nLoop+1])[0]    for nLoop in range(0,len(framesWavJuntos),2) ]
    
    wavArray= np.array(wavDataList)
    
    tempo = np.arange(start=0, stop= wavArray.size * deltaX, step= deltaX, dtype=np.float)
    

    
    arquivoWav = wave.open(nomeArquivoSaida, 'wb')
    arquivoWav.setnchannels(canais)
    arquivoWav.setsampwidth(objetoPyAudio.get_sample_size(formato))
    arquivoWav.setframerate(taxaDeAmostragem)
    arquivoWav.writeframes(framesWavJuntos)
    arquivoWav.close()  
            
    plt.plot(tempo,wavArray)
    plt.grid()
    plt.show()
            
    
    print("Fim de gravação")
    
    print ("Tipo streamMic: ", type(streamMic))
    print ("Tipo framesWav: ", type(framesWav))
    print ("Tipo framesWavJuntos: ", type (framesWavJuntos))
    print ("Tipo tempo: ", type(tempo))
    print ("Tipo deltaX: ", type(deltaX))
    print ("Tipo wavDataList: ", type(wavDataList))
    print ("Tipo wavArray: ", type(wavArray))
    
    

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
