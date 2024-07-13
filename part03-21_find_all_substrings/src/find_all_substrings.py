# Write your solution here
slowo = input("Proszę wpisać słowo: ")
znak = input("Proszę wpisać znak: ")

# Iteruj przez słowo, aby znaleźć wszystkie wystąpienia podanego znaku
index = 0
found = False

while index <= len(slowo) - 3:
    # Znajdź indeks następnego wystąpienia znaku
    index = slowo.find(znak, index)
    if index == -1:
        break
    # Sprawdź, czy po znalezionym znaku są co najmniej 2 znaki
    if index <= len(slowo) - 3:
        print(slowo[index:index + 3])
        found = True
    # Przejdź do następnego znaku, aby kontynuować wyszukiwanie
    index += 1

# Jeśli nie znaleziono żadnych podciągów, nic nie wypisuj
if not found:
    print()