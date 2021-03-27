def write_line_txt(a, c, m, seed, file_name):
    '''
    Funcion para escribir la lista de los valores de Xn, a, c, m y seed
    '''
    # Cargar el archivo y decidir como modificarlo
    f = open(file_name + ".txt", "a")
    # Escribe los valores
    f.write(str((a, c, m, seed)) + '\n')
    # Cierra el archivo guardando cambios
    f.close()
