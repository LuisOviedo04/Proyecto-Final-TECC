import numpy as np
import re
######FUNCIONES GENERALES #####

def crearMapa():   
    
    archivo = open("mapa.txt")
    data = archivo.read().strip()
    archivo.close()
 
    map_matriz = [[int(num) for num in line.strip().split()] for line in data.split('\n')]
    
    return map_matriz

def pedirMeta(mapa,lugares,pos_lugaresx,pos_lugaresy):
    menu(lugares)
    input('Presione cualquier tecla para seguir.')
    while True:
        opcion = int(input("Ingrese el indice de su lugar de destino: "))
        x = pos_lugaresx[opcion]
        y = pos_lugaresy[opcion]
        print('\n')
        if(mapa[int(x)][int(y)]==0):
            break

    meta = [int(x),int(y)]
    mapa[int(x)][int(y)] = 1
    input('Presione cualquier tecla para seguir.')
    return meta


######## FUNCIONES PARA RELLENAR EL MAPA ######

def rellenar(mapa,metax,personay):
    #arriba
    if(mapa[metax-1][personay]==0):
        mapa[metax-1][personay]=mapa[metax][personay]+1
            
        
    #abajo
    if(mapa[metax+1][personay]==0 ):
        mapa[metax+1][personay]=mapa[metax][personay]+1

        
    #derecha
    if(mapa[metax][personay+1]==0):
        mapa[metax][personay+1]=mapa[metax][personay]+1
        
    #izquierda
    if(mapa[metax][personay-1]==0):
        mapa[metax][personay-1]=mapa[metax][personay]+1



def numCeros(mapa):
    ceros = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if(mapa[i][j]==0):
                ceros = ceros+1
    return ceros

def cicloRellenar(mapa):
    ceros = numCeros(mapa)
    highVal = 0
    fin = False
    while(fin==False):
        highVal = highVal + 1      
        for i in range(len(mapa)-1):
            for j in range(len(mapa[0])-1):
                if(mapa[i+1][j+1]==highVal):
                                    
                    rellenar(mapa,i+1,j+1)
                    ceros = ceros - 1
                if(ceros==0):
                    fin = True
        


########### FUNCION PARA MOVER ESTUDIANTE ##########
def crearPersona(mapa,lugares,pos_lugaresx,pos_lugaresy):
    while True:
        opcion1 = int(input("Ingrese el indice de su lugar de origen: "))
        personax = pos_lugaresx[opcion1]
        personay = pos_lugaresy[opcion1]
        print('\n')
        if(mapa[int(personax)][int(personay)] != -1 and mapa[int(personax)][int(personay)] != 1):
            break

    mapa[int(personax)][int(personay)] = 0
    persona = [int(personax),int(personay)]
    
    return persona

def moverPersona(mapa,personax,personay,metax,metay,rutax,rutay):
        

    while(mapa[personax][personay] != mapa[metax][metay]):
        arriba = 1000
        abajo = 1000
        derecha = 1000
        izquierda = 1000
        if(mapa[personax-1][personay] >0):
            arriba = mapa[personax-1][personay] 
        if(mapa[personax+1][personay] >0):
            abajo = mapa[personax+1][personay]
        if(mapa[personax][personay+1] >0):
            derecha = mapa[personax][personay+1]
        if(mapa[personax][personay-1] >0):
            izquierda = mapa[personax][personay-1]

        values = np.array([arriba,abajo,derecha,izquierda])
        minimo = np.amin(values)

        #arriba
        if(mapa[personax-1][personay]==minimo):
            
            rutax.append(personax-1)
            rutay.append(personay)
            
            mapa[personax-1][personay]= 0
            personax = personax - 1

        #abajo
        if(mapa[personax+1][personay]==minimo ):
            
            rutax.append(personax+1)
            rutay.append(personay)
            
            mapa[personax+1][personay]= 0
            personax = personax + 1

        #derecha
        if(mapa[personax][personay+1]==minimo):
            
            rutax.append(personax)
            rutay.append(personay+1)
            
            mapa[personax][personay+1]= 0
            personay = personay + 1

        #izquierda
        if(mapa[personax][personay-1]==minimo):
            
            rutax.append(personax)
            rutay.append(personay-1)
            
            mapa[personax][personay-1]= 0
            personay = personay - 1
        
    
def imprimirRuta(rutax,rutay,pos_lugaresx,pos_lugaresy):
        
    print("Ruta de lugares para llegar a su destino.")
    
    for i in range(len(rutax)):
        for j in range(len(lugares)):
            if(rutax[i] == pos_lugaresx[j] and rutay[i] == pos_lugaresy[j]):
                print(lugares[j])
    
def menu(lugares):
    print("Lista de luegares disponibles.")
    for i in range(len(lugares)):
        print(i,'. ',lugares[i])

        
def automata(mapa,rutax,rutay):
    RegEx = re.compile(r'0+')
    cadena = []
    for i in range(len(rutax)):
        cadena.append(mapa[rutax[i]][rutay[i]])
            
    
    
    for i in range(len(cadena)):
        if RegEx.match(str(cadena[i])):
            valida = True
        else:
            print("Error: La ruta no es la optima")
            valida = False
            break

    if valida:
        print('La ruta correponde a la optima marcada por WaveFront')
        
        
############ MAIN ################

if __name__=="__main__":
    
    lugares = ['Biblioteca', 'Bloque A1', 'Bloque A2', 'Bloque A3',
   'Bloque A4', 'Bloque A5', 'Bohios 1', 'Bohios 2', 'Cafeteria', 'C. softbol', 
   'C. Futb.', 'Cons. Juridico', 'Entrada Prin.', 'Lab. Suelos', 
   'Offn. Financiera.', 'Papeleria', 'Parq. 1', 'Parq. 2', 'Parq. 3', 
   'Parq. 4', 'Parq. 5', 'Parq. Nuevo', 'Pd. Transcaribe.', 'Punt. Encuentro', 
   'Rectoria', 'Sal. Mamonal', 'Sali/Entr. Rodeo', 'Zona T']
    pos_lugaresx = [16,27,10,18,5,16,64,50,9,45,38,5,27,5,33,20,13,37,5,48,47,71,27,38,32,36,2,50]
    pos_lugaresy = [66,65,22,110,110,118,26,26,40,49,15,97,2,64,26,40,11,10,65,115,125,13,26,89,68,148,83,65]
    
    mapa = crearMapa()
    meta = pedirMeta(mapa,lugares,pos_lugaresx,pos_lugaresy)
    metax = meta[0]
    metay = meta[1]
    cicloRellenar(mapa)
    persona = crearPersona(mapa,lugares,pos_lugaresx,pos_lugaresy)
    personax = persona[0]
    personay = persona[1]
    rutax = []
    rutay = []    
    
    moverPersona(mapa,personax,personay,metax,metay,rutax,rutay)
    imprimirRuta(rutax,rutay,pos_lugaresx,pos_lugaresy)  
    
    automata(mapa,rutax,rutay)
    