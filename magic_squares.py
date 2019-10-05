##############################################################
#							     #
#	Solucionador de cuadrados magicos con backtracking   #
#							     #
#	Dennis Alberto Mendoza Solis			     #
#	dms.albertmend@gmail.com			     #
#	Programacion Avanzada, PCIC UNAM		     #
#	10 de septiembre, 2019				     #
#							     #
##############################################################

#Numpy 	-> Operaciones matematicas
import numpy as np
#Time	-> Manejo de tiempo
import time
#Opencv -> Visualizacion
import cv2

#tamano del cuadrado magico (nxn)
n=3

#tamano de la imagen
size=100*n
#inicializacion de la imagen
img = np.zeros((size,size,3),np.uint8)
#tipo de fuente en la imagen
font = cv2.FONT_HERSHEY_SIMPLEX
#tamano de la fuente
if n<=3:
	fontsize=3
else:
	fontsize=2.5
#color de la fuente
fontcolor=(255,255,255)
	    

#inicializaciones
opciones=[]
cuad_mag=np.zeros(n*n)
#calculo de la constante magica
k=n*(np.power(n,2)+1)/2

# funcion que revisa si el cuadrado magico c
# es una solucion completa, si lo es regresa True
def solucion_completa(c):
    #si alguna columna esta llena y no suma k, False
    #si alguna columna no esta llena, False
    for i in range(0,n):
        columna=[]
        for j in range(i,n*n,n):
            columna.append(c[j])
        if 0 not in columna:
            if np.sum(columna)!=k:
                return False
        else:
            return False

    #si alguna fila esta llena, y no suma k, False
    #si alguna fila no esta llena, False
    for i in range(0,n):
        if 0 not in c[i*n:(i+1)*n]:
            if np.sum(c[i*n:(i+1)*n])!=k:
                return False
        else:
            return False

    #si la diag135 esta llena y no suma k, False
    #si la diag135 no esta llena, False
    i=0
    diag135=[]
    while i<n*n and c[i]!=0:
        diag135.append(c[i])
        i+=n+1 
    if i>n*n:
        if np.sum(diag135)!=k:
            return False
    else:
	return False

    #si la diag45 esta llena y no suma k, False
    #si la diag45 no esta llena, False
    i=n-1
    diag45=[]
    while i<=n*n-n and c[i]!=0 and i!=0:
        diag45.append(c[i])
        i+=n-1 
    if i>n*n-n:
        if np.sum(diag45)!=k:
            return False
    else:
	if n==1 and c[0]==1:
		return True
	else:
		return False

    #si llega a este punto, la solucion es completa
    return True

# funcion que revisa si la opcion op es aceptable para
# el cuadrado magico c
def aceptable(c,op):
    #encontramos la posicion donde se insertaria el numero
    i=0
    while i<len(c)-1 and c[i]!=0:
        i+=1
    c[i]=op
    #si alguna columna esta llena y no suma k, False
    #si alguna columna no esta llena, que sume <k
    for i in range(0,n):
        columna=[]
        for j in range(i,n*n,n):
            columna.append(c[j])
        if 0 not in columna:
            if np.sum(columna)!=k:
                return False
        else:
            if np.sum(columna)>=k:
                return False
    #si alguna fila esta llena y no suma k, False
    #si alguna fila no esta llena, que sume <k
    for i in range(0,n):
        if 0 not in c[i*n:(i+1)*n]:
            if np.sum(c[i*n:(i+1)*n])!=k:
                return False
        else:
            if np.sum(c[i*n:(i+1)*n])>=k:
                return False
                
    #si la diag135 esta llena, que sume k
    #si la diag135 no esta llena, que sume <k
    i=0
    diag135=[]
    while i<n*n and c[i]!=0:
        diag135.append(c[i])
        i+=n+1 
    if i>n*n:
        if np.sum(diag135)!=k:
            return False
    else:
        if np.sum(diag135)>=k:
            return False
	
    #si la diag45 esta llena, que sume k
    #si la diag45 no esta llena, que sume <k	
    i=n-1
    diag45=[]
    while i<=n*n-n and c[i]!=0 and i!=0:
        diag45.append(c[i])
        i+=n-1 
    if i>n*n-n:
        if np.sum(diag45)!=k:
            return False
    else:
	if np.sum(diag45)>=k:
	    return False   
    #si llega a este punto, la solucion es aceptable 
    return True
    
# funcion que obtiene todas las soluciones para un cuadrado magico
# cm por medio de backtracking
def backtracking(cm):
    exito=False
    # inicializamos las opciones, que son todos aquellos numeros 
    # entre 1 y n2 que no estan en cm
    opciones=[]
    for num in range(1,np.power(n,2)+1):
        if num not in cm:
            opciones.append(num)
    # mientras tengamos opciones      
    while opciones!=[]:
	# obten la primera opcion
        opcion=opciones.pop(0)
	# esperar 0.1s entre cada iteracion, para observar como
	# evoluciona la solucion	
	#time.sleep(0.1)        
	# si la opcion es aceptable	
	if aceptable(list(cm),opcion):
            # coloca la opcion como el siguiente numero
            i=0
            while i<len(cm)-1 and cm[i]!=0:
                i+=1
            cm[i]=opcion
            # manda a pantalla la solucion actual 
	    # print cm
	    ##########################	VISUALIZACION	################################################
	    '''img = np.zeros((size,size,3),np.uint8)
	    for ii in range(n):
		for jj in range(n):
		    cv2.rectangle(img, (ii*int(size/n),jj*int(size/n)),
				 (ii*int(size/n)+int(size/n),jj*int(size/n)+int(size/n)),
				 (0, 255, 0), 2) 
		    cv2.putText(img,str(int(cm[ii*n+jj])),(ii*int(size/n)+int(0*size/n),
				jj*int(size/n)+int(0.7*size/n)), font,fontsize,fontcolor,2) 
	
	    cv2.imshow('image',img)
	    kk=cv2.waitKey(10) & 0XFF'''
	    ##########################	VISUALIZACION	################################################
	
	    # si la solucion es completa, la anotamos
	    if  solucion_completa(cm):
		# esperamos dos segundos antes de seguir con el proceso
		# para que el usuario pueda ver la solucion completa actual
                time.sleep(2)
 		soluciones_completas.append(list(cm))
                print '------------'
		for x in range(0,n):
			print cm[x*n:x*n+n]
		cm[i]=0
            else:
		# si la solucion no es completa, continuamos con el backtracking
                exito=backtracking(cm)
		# si ese movimiento no llevo a ninguna solucion, quitamos el 
		# movimiento y probamos con otra opcion
                if exito==False:
                    cm[i]=0
    #si llegamos aqui, el programa ha terminado de calcular todas las soluciones
    return exito

soluciones_completas=[]
backtracking(cuad_mag)
print '\n\nSOLUCIONES FINALES:'
for i in range(0,len(soluciones_completas)):
	print '------------'
	for x in range(0,n):
		print map(int,soluciones_completas[i][x*n:x*n+n])
