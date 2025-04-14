import matplotlib.pyplot as plt

class Collatz:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def collatz_sequence(self, n):
        iterations = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            iterations += 1
        return iterations
    
    def run(self):
        results = []
        for num in range(self.min_value, self.max_value + 1):
            iterations = self.collatz_sequence(num)
            results.append((num, iterations))
        return results

def plot_collatz(results):
    # Separa los resultados en dos listas: números y sus iteraciones
    numbers, iterations = zip(*results)

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(iterations, numbers, color='blue', s=1)
    plt.title('Conjetura de Collatz: Número de Iteraciones vs Número Inicial')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Número Inicial')
    plt.grid(True)
    plt.show()

# Crear la instancia de la clase Collatz para los números entre 1 y 10000
collatz_calculator = Collatz(1, 10000)

# Ejecutar el cálculo de iteraciones
collatz_results = collatz_calculator.run()

# Graficar los resultados
plot_collatz(collatz_results)
