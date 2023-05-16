# Napisz funkcję, która zapisuje dane (np. słownik lub listę) do pliku JSON. Funkcja
# powinna przyjmować dwa argumenty: dane do zapisania i nazwę pliku. Użyj metody
# json.dump() do zapisania danych. Testuj swoją funkcję, zapisując dowolne dane do
# pliku
import json
def json_to_file(data, file):
    with open(file, mode="w") as file:
        file.write(data)

def to_json(data):
    return json.dumps(data)

json_to_file(to_json([1,'dd',3]),"json.txt")
