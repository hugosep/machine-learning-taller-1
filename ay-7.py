enviado = ["casa", "asa",
    "camisa", "camicha",
    "objeto", "ojeto",
    "zafiro", "afío"
    ]

i = 0
transcripciones = list()

while i < len(enviado) - 1:
    transcripciones.append( (enviado[i], enviado[i + 1]) )
    i += 2

transcripciones = list()

for i in range(0, len(enviado)-1, 2):
    transcripciones.append( (enviado[i], enviado[i + 1]) )

print(transcripciones)

nuevas_transcripciones = list()

i = 0

while i < len(transcripciones):
    palabra, t = transcripciones[i]
    
    nuevas_transcripciones.append(palabra)
    nuevas_transcripciones.append(t)

    i += 1

print(nuevas_transcripciones)
