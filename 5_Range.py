#Lo mas importante es que range no es mutable
#asi que solo se puede modificar al momento de su creacion 
#su estructura es range(inicio,fin,paso) basicamente
range(5)
print(list(range(5))) 
#con list nos crea una lista con los numeros
#asi que creara la sucesion de numeros terminando en n y no incluyendo n
# n-1  asi que si quisiera que fuera 5 y no 4 tendria que poner un 6 en el parametro 

x= list(range(2,21,2)) #inicio , final , incrementos
print(x) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

x.insert(0,1) #inserta en la posicion 0 el valor 1
print(x) #[1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]