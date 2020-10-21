# Scooter kosten

km_per_maand = ""
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2


def bereken_maandkosten(km_per_maand):
    return (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand


while not isinstance(km_per_maand, float):   
    try:
        km_per_maand = input("Hoeveel Kilometer rij je?: ")
        km_per_maand = float(km_per_maand)
        print("Je betaald" ,bereken_maandkosten(km_per_maand),"euro per maand.")
    except ValueError:
        print(km_per_maand + " Is geen geldig getal!")
