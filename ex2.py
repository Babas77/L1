def vol(a):
    """
    Calcule récursivement le temps de vol de
    la suite de Syracuse avec le terme initial a.
    
    :param int a : terme initial
    :return int n : le plus petit indice n tel que un = 1
    """
    if a < 1:
        return "[-] Terme initial inférieur à 1 !"
    elif a == 1:
        return 0
    else:    
        if a % 2 == 0:
            return vol(a/2) + 1
        else:
            return vol(3*a+1) + 1 

if __name__ == "__main__":
    a = int(input("Saisir a : "))
    print(vol(a))
