# Zaimportuj moduł json. Następnie utwórz prosty słownik Pythona zawierający nastę-
# pujące pary klucz-wartość: 'name': 'Jan', 'age': 30, 'city': 'Warszawa'. Użyj
# metody json.dumps(), aby przekonwertować ten słownik na łańcuch JSON, a następnie
# wydrukuj wynik.
import json
dict ={
        'name': 'Jan',
        'age': 30,
        'city': 'Warszawa'
    }

print(type(dict))

str_ = json.dumps(dict)
print(str_[1])

dict_val = json.loads(str_)
print(type(dict_val))