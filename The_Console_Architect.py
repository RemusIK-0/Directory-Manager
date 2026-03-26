import matplotlib.pyplot as plt

# Graphic for inserted values of CPU usage in percentage over time (1 min, 2 min, 3 min, 4 min, 5 min)
def grafic():
    cpu_data = []
    minutes = ["1 min", "2 min", "3 min", "4 min", "5 min"]

    for i in minutes :
        while True:
            try:
                value = input(f"Introduceti date relevante in procente (%) pentru valoarea: {i}\n")
                cpu_data.append(int(value))
                break
            except ValueError:
                print("Va rugam introduceti o valoare numerica")
    plt.figure()
    plt.plot(minutes, cpu_data, marker='o', linestyle='-', color='g', label='Utilizare CPU')

    plt.title("Temperatura CPU")
    plt.xlabel("Timp")
    plt.ylabel("Utilizare %")
    plt.grid(True)
    plt.legend()
    plt.show()

grafic()