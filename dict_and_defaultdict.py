# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:08:37 2020

@author: VicFabrice
"""

# Some friend (jjconti) told me I should check defaultDict, so first I went over
# simple dictionaries and then I put hands on defaultDict, which is not a type
# It's more like a bunch of functions really useful to handle dictionaries 

#I keep mixing spanish and english, I'm not sorry though
testDict = {
        "unaKey": "unValue",
        "otraKey": "otroValue",
        "ultimaKey": "ultimoValue"
        }

#accessing
accedido = testDict["unaKey"]
print("Value for key 'unaKey' is ", accedido)

# When you ask for the value of an inexistent key, you get a key error
#print(testDict["noExiste"]) 

# changing value of an existing key
testDict["ultimaKey"] = "valueCambiado"
print("Printing the whole dict ", testDict)

#iterar un dict
#imprime todos los keys (no los values)

for k in testDict:
    print("Pinting all keys ",k)
#mprime todos los values  
for v in testDict:
    print("Printing all values ", testDict[k])
    
#otra forma de imprimir values
for v in testDict.values():
    print("Value is ", v)

#iterar keys and v
print("Key and value pairs \n")
for k,v in testDict.items():
    print(k,v)
    
#chequear si K existe
if "unaKey" in testDict:
    print("Existe la key unaKey")

#add items
testDict["nuevaKey"] = "nuevoValue"
print("Add a kv pair ", testDict)

#remover un item por key
testDict.pop("nuevaKey")
#print(testDict)

print("Here comes the fun part\n")
#So, defaultDict is a way to avoid exceptions but the type stays the same
#That's the way you create a empty dictionary
testDefaultDict = {}
#Obviously if you try to look up for a key, you get an error 'cause dict is
#still empty
#key error  print(testDefaultDict["key inexistente"])
#Well, that's the thing my friend told me about: setdefault and get

#setdefault => if key isnt in the dict, saves key and value is default value
# => if key is in the dict, setdefault doesnt do anything
testDefaultDict.setdefault('keyBuscada', 'defaultKey')
print(testDefaultDict['keyBuscada'])

#What's get? if key isnt in the dict, 
#Get devuelve el default value si el valor no existe, pero no agrega nada al dict
testDefaultDict2 = {}
testDefaultDict2.get('key inexistente', 'default_value')
print("Cree un dict vacío y le pedí un key q no existe ", testDefaultDict2) #devuelve el dict vacío
#Si el valor existe, entonces get no hace nada
testDefaultDict2["unaKey"] = "unValue"
print(testDefaultDict2.get('key inexistente'))
print(testDefaultDict2.get('unaKey', 'default_Value'))















