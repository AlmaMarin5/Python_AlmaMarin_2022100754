#introduccion a la lista
array=["futbol", "Pc", 18.6,18,[6,7,10.4],True,False]
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])
#cantidad de datos que cuenta el array
print(len(array))
#agregar un valor dentro de la lista
array.append(66)
print(array)
#insertar datos en una posicion
array.insert(1,88)
print(array)
#insertar mas de un dato al final
array.extend([1,88,True,100])
print(array)



array1=["futbol", "Pc", 18.6,18,[6,7,10.4],True,False,"Pc"]
array2=[200,250,"hola"]
array3=array1+array2
print(array3)
#buscar valores dentro de un array
print("Pc" in array1)
#saber el indice donde esta lo que busco
print(array1.index("Pc"))
#cantidad de veces que tengo el valor en mi array
print(array1.count("Pc"))
#borrar valores de un array
array1.remove("Pc")
print(array1)
#limpiar
#array1.clear()
print(array1)
#cambiar la posicion
array1.reverse()
print(array1)
#ordenar de mayor a menor
array4=[1,2,8,-11,5]
array4.sort()
print(array4)
array4.sort(reverse=True)
print(array4)

