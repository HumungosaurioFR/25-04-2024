Urbanom2 = 25000
Permiso_urbano = 0.45
Comercialm2 = 60000
Permiso_comercial = 0.75
Campestrem2 = 35000
Permiso_campestre = 0.15

list_urbano = []
list_comercial = []
list_campestre = []

import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Juan Esteban Aristizábal Suárez')
    print('Fecha: 25 de abril del 2024\n')

def fnt_registrar(nombre, ancho, largo, tipo_lote):
    if tipo_lote == "Urbano":
        valor_mt2 = Urbanom2
        permiso_construccion = Permiso_urbano
    elif tipo_lote == "Comercial":
        valor_mt2 = Comercialm2
        permiso_construccion = Permiso_comercial
    elif tipo_lote == "Campestre":
        valor_mt2 = Campestrem2
        permiso_construccion = Permiso_campestre

    area = ancho * largo
    valor_lote = area * valor_mt2
    valor_permiso = valor_lote * permiso_construccion
    print(f'El valor del lote es: {valor_lote:.2f}')
    print(f'El valor del permiso de construcción es: {valor_permiso:.2f}')
    print(f'El valor total es: {valor_lote + valor_permiso:.2f}')

def fnt_selector(op):
    global sw
    fnt_limpiar()
    if op == '1':
        nombre = input('Nombre: ')
        ancho = float(input("Ingrese el ancho del lote (en metros):  "))
        largo = float(input("Ingrese el largo del lote (en metros):  "))
        tipo_lote = input('Lotes:\n1. Urbano\n2. Comercial\n3. Campestre\n--> ')
        if tipo_lote == "1":
            fnt_limpiar()
            tipo_lote = "Urbano"
            R = {'Nombre': nombre, 'Area': ancho * largo, 'Tipo de lote': tipo_lote}
            list_urbano.append(R)
        elif tipo_lote == "2":
            fnt_limpiar()
            tipo_lote = "Comercial"
            R = {'Nombre': nombre, 'Area': ancho * largo, 'Tipo de lote': tipo_lote}
            list_comercial.append(R)
        elif tipo_lote == "3":
            fnt_limpiar()
            tipo_lote = "Campestre"
            R = {'nombre': nombre, 'Area': ancho * largo, 'Tipo de lote': tipo_lote}
            list_campestre.append(R)
        fnt_registrar(nombre, ancho, largo, tipo_lote)
        enter = input('<ENTER>')
    elif op == '2':
        fnt_limpiar()
        print('Lotes Urbanos:')
        for lote in list_urbano:
            print(lote)
        print('Lotes Comerciales:')
        for lote in list_comercial:
            print(lote)
        print('Lotes Campestres:')
        for lote in list_campestre:
            print(lote)
        enter = input('<ENTER>')
    elif op == '3':
        sw = False

sw = True
while sw == True:
    fnt_limpiar()
    op = input('\n<<< MENU PRINCIPAL >>>>\n\n1. Registrar Lote\n2. Mostrar Lotes\n3. Salir\n\n-> ')
    fnt_selector(op)