meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LMAO": "Una respuesta a algo muy gracioso",
            "ASAP": "tan pronto como sea posible",
            "BRB":  "es como decir que vuelves en un momento"
            }
palabras = input("escribe una palabra que no entiendas (en mayusculas): ")
if palabras in meme_dict.keys():
    print(meme_dict[palabras])
else:
    print("error, palabra no encontrada")
    
