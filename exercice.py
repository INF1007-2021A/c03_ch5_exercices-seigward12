#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number <0:
        number*=-1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms=''
    for letter in prefixes:
        noms=noms+letter+suffixe+','
        
    return [noms]


def prime_integer_summation() -> int:
    return 0
    nb_primeNumber=0
    number=2
    summation=0
    while nb_primeNumber<=100:
        for i in range(2,number):
            if number%i==0:
                number+=1
                continue
    return summation


def factorial(number: int) -> int:
    somme=1
    for i in range(1,number+1):
        somme*=i
    return somme


def use_continue() -> None:
    for i in range(1,11):
        if i==5:
            continue
        else:
            print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    listeDacceptance=[]
    for personnes in groups:
        if len(personnes)>3 and len(personnes)<=10:
            listeDacceptance.append(True)
        else:
            listeDacceptance.append(False)
        print(listeDacceptance)

    i=0
    for personnes in groups:
        if listeDacceptance[i]==False:
                continue
        for age in personnes:
            if age==25:
                listeDacceptance[i]=True
        i+=1
    i=0
    for personnes in groups:
        if listeDacceptance[i]==True:
                continue
        for age in personnes:
            if age<18:
                listeDacceptance[i]=False
        i+=1

    i=0
    for personnes in groups:
        if listeDacceptance[i]==True:
                continue
        for age in personnes:
            if age==50:
                for age in personnes:
                    if age>70:
                        listeDacceptance[i]=False
        i+=1

    return listeDacceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
