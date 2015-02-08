from string import ascii_lowercase

# { key:value for item in list if conditional }


dict_comp = { item:ord(item) for item in ascii_lowercase }

print dict_comp

lista = ['jeden','dwa','samochod','miejscowosc']

dict_comp = [slowo for slowo in lista if len(slowo)>5]

print dict_comp