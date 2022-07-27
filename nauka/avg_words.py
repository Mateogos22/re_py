# Wprowadzam tekst, który chcę sprawdzić
text = input('Podaj tekst artykułu: ')

# Liczę ilość znaków w podanym tekście 
characters = len(text)

# Liczę ilość słów
words = len(text.split())

# Dzielę liczbę znaków przez liczbę słów
avg_words = (characters / words) - 1

# Drukuję średnią liczbę znaków w tekście
print('Tekst ma', avg_words, 'znaków')
