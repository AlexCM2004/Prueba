from collections import deque

# Definición de la estructura de datos para un proceso
class Proceso:
    def __init__(self, nombre, llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.llegada = llegada
        self.tiempo_ejecucion = tiempo_ejecucion

# Lista de procesos
procesos = [
    Proceso("P1", 0, 10),
    Proceso("P2", 2, 5),
    Proceso("P3", 4, 7)
]

quantum = 4  # Quantum en milisegundos
tiempo_actual = 0
cola = deque(procesos)  # Cola de procesos

while cola:
    proceso_actual = cola.popleft()
    if proceso_actual.tiempo_ejecucion <= quantum:
        # El proceso se ejecuta completamente
        print(f"Tiempo {tiempo_actual} ms: {proceso_actual.nombre} (Tiempo restante: 0 ms)")
        tiempo_actual += proceso_actual.tiempo_ejecucion
    else:
        # El proceso se ejecuta por un quantum y luego vuelve a la cola
        print(f"Tiempo {tiempo_actual} ms: {proceso_actual.nombre} (Tiempo restante: {proceso_actual.tiempo_ejecucion - quantum} ms)")
        tiempo_actual += quantum
        proceso_actual.tiempo_ejecucion -= quantum
        cola.append(proceso_actual)

print("Todos los procesos han terminado.")
