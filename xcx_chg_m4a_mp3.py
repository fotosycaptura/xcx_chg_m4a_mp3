from pydub import AudioSegment
import os
print("Script para convertir m4a a mp3...")

contenido = os.listdir("./")
audios = []
for fichero in contenido:
    if os.path.isfile(os.path.join("./", fichero)) and fichero.endswith('.m4a'):
        print(f"Procesando {fichero} ...")
        mp3_audio = AudioSegment.from_file(fichero, format="m4a")
        fichero_final = fichero[0:fichero.find(".m4a")] + ".mp3"
        mp3_audio.export(fichero_final, format="mp3")
        print(f"{fichero} convertido a mp3...")
