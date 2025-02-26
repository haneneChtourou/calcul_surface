# main.py

from geometry import volume_sphere, volume_cylinder, volume_cone, volume_cube

def main():
    print("Bienvenue dans le programme de calcul de volumes géométriques!")

    while True:
        print("\nChoisissez une forme géométrique:")
        print("1. Sphère")
        print("2. Cylindre")
        print("3. Cône")
        print("4. Cube")
        print("5. Quitter")
        
        choice = input("Entrez votre choix (1/2/3/4/5): ")
        
        if choice == '1':
            try:
                radius = float(input("Entrez le rayon de la sphère: "))
                volume = volume_sphere(radius)
                print(f"Le volume de la sphère est: {volume:.2f}")
            except ValueError as e:
                print(f"Erreur: {e}")

        elif choice == '2':
            try:
                radius = float(input("Entrez le rayon du cylindre: "))
                height = float(input("Entrez la hauteur du cylindre: "))
                volume = volume_cylinder(radius, height)
                print(f"Le volume du cylindre est: {volume:.2f}")
            except ValueError as e:
                print(f"Erreur: {e}")

        elif choice == '3':
            try:
                radius = float(input("Entrez le rayon du cône: "))
                height = float(input("Entrez la hauteur du cône: "))
                volume = volume_cone(radius, height)
                print(f"Le volume du cône est: {volume:.2f}")
            except ValueError as e:
                print(f"Erreur: {e}")

        elif choice == '4':
            try:
                side = float(input("Entrez la longueur du côté du cube: "))
                volume = volume_cube(side)
                print(f"Le volume du cube est: {volume:.2f}")
            except ValueError as e:
                print(f"Erreur: {e}")

        elif choice == '5':
            print("Merci d'avoir utilisé le programme de calcul de volumes. À bientôt!")
            break

        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    main()
