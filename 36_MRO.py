#Method Resolution order / resolucion de ordenes de metodos

#La funcion Super busca siguiendo el orden MRO delegando en la primer clase superior por encima de la
#clase a la que pertence hasta encontrar el metodo qe estamos indicando
#es basicamento con lo que jugue en el 35_HerenciaMultipleSp.py
# poner una clase antes que otra o solo poner una clase, igual la encuentra 

#Siguiendo la secuencia MRO comienza por buscar desde la clase donde se encuentra la invocacion de super 
#al metodo de sus padres, los padres de sus padres y asi hasta alcanzar la clase Object- la principal 
#ejemplo 

#no
#es basicamente el desmadre de intercambiar los metodos de una clase con otra que hice en el pasado 35
#pastor antes de cachi o algo asi

#en conclucion 
#EL ORDEN DE LAS CLASES IMPORTAN !!

