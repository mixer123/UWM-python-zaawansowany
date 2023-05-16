# Zaimportuj moduł json oraz bibliotekę NumPy. Utwórz tablicę NumPy o wymiarach
# 2x2x2, wypełnioną losowymi liczbami. Następnie użyj metody json.dumps() do prze-
# konwertowania tej tablicy na łańcuch JSON, przekształcając najpierw tablicę na listę
# za pomocą metody tolist(). Użyj argumentu indent=4, aby sformatować wynikowy
# łańcuch JSON dla lepszej czytelności. Wydrukuj wynik.

import json
import pandas as pd
import numpy as np
matrix_ = np.array([(1,2,3),(3,4,5),(6,7,8)])
print(matrix_.tolist())
matrix_to_json = json.dumps(matrix_.tolist())
print(matrix_to_json)

