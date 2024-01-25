from prostokat import Prostokat, Kwadrat
from trojkat import Trojkat, TrojkatRownoramienny, TrojkatRownoboczny, TrojkatRoznoboczny


if __name__ == "__main__":
    liczby = []
    figury = []
    try:
        with open("dane.txt", "r") as dane:
            for linia in dane:
                linia = linia.strip().split()
                zestaw = []
                for liczba in linia:
                    zestaw.append(float(liczba))
                liczby.append(zestaw)
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    if len(liczby) == 0:
        print("Brak danych do przetworzenia.")
    else:
        for zestaw in liczby:
            if 0 not in zestaw:
                if len(zestaw) == 3:
                    a, b, c = zestaw[:3]
                    if a + b > c and a + c > b and b + c > a:
                        if a == b == c:
                            figury.append(TrojkatRownoboczny(a, b, c))
                        elif a == b or a == c or b == c:
                            figury.append(TrojkatRownoramienny(a, b, c))
                        else:
                            figury.append(TrojkatRoznoboczny(a, b, c))
                elif len(zestaw) == 2:
                    a, b = zestaw[:2]
                    figury.append(Prostokat(a, b))
                elif len(zestaw) == 1:
                    a = zestaw[0]
                    figury.append(Kwadrat(a))
    print("\nFigury przed sortowaniem:")
    for figura in figury:
        print(repr(figura))
    figury.sort(reverse=True)
    print("\nFigury po sortowaniu:")
    for figura in figury:
        print(repr(figura))