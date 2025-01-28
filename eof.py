def cargar_buffer(entrada, inicio, tamano_buffer):
    fin = inicio + tamano_buffer
    buffer = entrada[inicio:fin]
    if len(buffer) < tamano_buffer:
        buffer += ["eof"]
    return buffer

def procesar_buffer(buffer, lexema_incompleto=""):
    lexemas = []
    lexema = lexema_incompleto
    for char in buffer:
        if char.isspace() or char == "eof":
            if lexema:
                lexemas.append(lexema)
                lexema = ""
            if char == "eof":
                break
        else:
            lexema += char
    return lexemas, lexema

def simular_procesamiento(archivo, tamano_buffer):
    with open(archivo, 'r') as f:
        entrada = list(f.read())
    
    inicio = 0
    lexema_incompleto = ""
    
    while True:
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)
        lexemas, lexema_incompleto = procesar_buffer(buffer, lexema_incompleto)
        
        for lexema in lexemas:
            print(f"Lexema procesado: {lexema}")
        
        if "eof" in buffer:
            break
        
        inicio += tamano_buffer

simular_procesamiento("archivo.txt", 10)
