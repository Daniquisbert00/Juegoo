import random 
opciones=["piedra", "papel","tijeras"]
magia=random.randint(0,2)
compu=opciones[magia]
print("Eleccion de la computadora", compu)
tu=input("opcion: ")
print("Tu eleccion fue: ",tu)

if (tu == compu):
    print("Empate: ")
    
if (tu == "tijeras"):
    if(compu =="papel"):
        print("ganaste")
    if(compu == "piedra"):
        print("perdiste")
    
if (tu == "papel"):
    if(compu == "piedra"):
        print("ganaste")
    if(compu == "tijeras"):
        print("perdiste")
        
if (tu == "piedra"):
    if(compu =="tijeras"):
        print("ganaste")
    if(compu == "papel"):
        print("perdiste")
        
        
        