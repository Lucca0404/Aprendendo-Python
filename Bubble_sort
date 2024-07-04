def bubble_sort(lista):
    tamanho = len(lista)
    while tamanho > 1:
        i = 1
        while i < tamanho:
            if lista[i] < lista[i-1]:
                lista[i],lista[i-1] = lista[i-1],lista[i]
            i+=1
        tamanho-=1

def main():
    lista = [10,9,8,7,6,5,4,3,2,1]
    bubble_sort(lista)
    print(lista)

if __name__=='__main__':
    main()
