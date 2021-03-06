import pyaudio
import wave
def reproducao_audio(audio):
    """Metodo de reprodução do aúdio"""
    chunk = 1024
    wf = wave.open(audio, 'rb') #Abertura
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)
    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()