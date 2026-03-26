from The_Console_Architect import grafic
import os
import shutil

# Main menu for the console application
def start_app():
    while True:
        print("#### Meniu Principal ####\n")
        print("1. Afiseaza Grafic CPU")
        print("2. Organizare fisiere")
        print("3. Exit")

        choice = input("Introdu optiunea dorita: ").strip()
        # Function for sorting files in the current directory
        def sort_files():
            print("\n### Organizator Fisiere ###\n")
            print("1. Vizualizare fisiere")
            print("2. Creeaza un fisier nou")
            print("3. Sorteza fisiere manual")
            print("4. Sorteaza Fisiere pe Categorii prestabilite(.jpg, .txt, etc.)")
            print("5. Exit")
            sort_files_choice = input("Alege optiunea dorita: ").strip()
            if sort_files_choice == "1":
                print("\n## Lista Foldere ##\n")
                os.listdir()
            elif sort_files_choice == "2":
                new_dir = input("\nIntrodu numele fisierului: ")
                os.makedirs(new_dir, exist_ok=True)
                if new_dir:
                    print("\nFolder creat cu succes")
            elif sort_files_choice == "3":
                source = input("\nScrieti numele fisierului sursa: ").strip()
                destination = input("Scrieti numele fisierului destinatie: ").strip()
                os.makedirs(destination, exist_ok=True)
                shutil.move(source, destination)
                if destination:
                    print(f"\nFisierul {source} a fost mutat in folderul {destination}")
            elif sort_files_choice == "4":
                PATH = (f"{os.curdir}/app_necesities")
                standard_categories = ["jpg", "txt", "json", "csv"]
                for i in standard_categories:
                    os.makedirs(os.path.join(PATH, f"fisiere {i}"), exist_ok=True)
                    for file in os.listdir(PATH):
                        if file.endswith(f".{i}"):
                            shutil.move(f"{PATH}/{file}", f"{PATH}/fisiere {i}")
            else:
                return
            
        if choice == "1":
            grafic()
        elif choice == "2":
            sort_files()
        elif choice == "3":
            break
        elif choice == "bonus":
            print("Inca nu m-am gandit la un Easter Egg")
        else: 
            print("Introduceti o optiune valida")

start_app()
