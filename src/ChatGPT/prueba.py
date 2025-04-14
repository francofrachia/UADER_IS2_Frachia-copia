"""Este módulo contiene funciones para procesar datos de prueba."""

import os
from openai import OpenAI

try:
    import readline
except ImportError:
    try:
        import pyreadline3 as readline
    except ImportError:
        readline = None
        print("No se pudo importar readline para historial.")

HISTORIAL_PATH = "historial_chat.txt"


if readline and os.path.exists(HISTORIAL_PATH):
    try:
        readline.read_history_file(HISTORIAL_PATH)
    except Exception as e:
        print("No se pudo leer el historial:", e)


client = OpenAI(api_key=os.getenv("sk-proj-esopVz6LSwFJT7-vICYXyJUfnyzA8HK2VxMymvRzJpq5XRO6IN1" \
"jaa1QLP1mAgLgT6VSOFcUEcT3BlbkFJBu1gz14nPqGc3U2t0aNfkXnnf9_0yNwdtMoWZzCXQbkwmk6-hmOiHeULffMp5F" \
"5AY5F3UNV4sA"))

print("Escribí tus consultas para chatGPT. Escribí 'salir' para terminar.")

while True:
    try:
        consulta = input(">> ").strip()
        if consulta.lower() == "salir":
            break

        if not consulta:
            print("Ingresá una consulta válida.")
            continue

        if readline:
            readline.add_history(consulta)

        CONSULTA_FORMATEADA = f"You: {consulta}"
        print(CONSULTA_FORMATEADA)

        try:
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "user", "content": CONSULTA_FORMATEADA}
                ]
            )
            respuesta = response.choices[0].message.content.strip()
            print(f"chatGPT: {respuesta}")
        except Exception as e:
            print("Error al consultar la API:", e)

    except KeyboardInterrupt:
        print("\nFinalizado por el usuario.")
        break
    except Exception as e:
        print("Error inesperado:", e)

if readline:
    try:
        readline.write_history_file(HISTORIAL_PATH)
    except Exception as e:
        print("No se pudo guardar el historial:", e)

# fhjsdkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfsaklfafhsdfajhalkf
# jhadsfjsdklfhklhljalskjfhsdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjf
# hdsaklfjahkhklahkajjkfsaklfafhsdfajhalkfjhadsfjsdklfhklhljals
# kjfhsdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjk
# fsaklfafhsdfajhalkfjhadsfjsdklfhklhljalskjfhsdjlsdjfjjkakljfh
# jsdkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfsaklfafhsdfajhalkfjh
# adsfjsdklfhklhljalskjfhsdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhd
# saklfjahkhklahkajjkfsaklfafhsdfajhalkfjhadsfjsdklfhklhljalskj
# fhsdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfs
# aklfafhsdfajhalkfjhadsfjsdklfhklhljalskjfhsdjlsdjfjjkakljfhjs
# dkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfsaklfafhsdfajhalkfjhad
# sfjsdklfhklhljalskjfhsdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhdsa
# klfjahkhklahkajjkfsaklfafhsdfajhalkfjhadsfjsdklfhklhljalskjfh
# sdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfsak
# lfafhsdfajhalkfjhadsfjsdklfhklhljalskjfhsdjlsdjfjjkakljfhjsdk
# fjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfsaklfafhsdfajhalkfjhadsf
# jsdklfhklhljalskjfhsdjlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhdsakl
# fjahkhklahkajjkfsaklfafhsdfajhalkfjhadsfjsdklfhklhljalskjfhsd
# jlsdjfjjkakljfhjsdkfjhdsakfjhsdkjfhdsaklfjahkhklahkajjkfsaklf
# afhsdfajhalkfjhadsfjsdklfhklhljalskjfhsdjlsdjfjjkakljfhjsdkfj
# hdsakfjhsdkjfhdsaklfjahkhklahkajjkfsaklfafhsdfajhalkfjhadsfjs
# dklfhklhljalskjfhsdjlsdjfjjkaklj
#comentario final