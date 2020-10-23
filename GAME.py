import random

words_bank = [
   'автострада', 'бензин', 'инопланетянин',
   'самолет', 'библиотека', 'шайба', 'олимпиада'
]

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
   letter = input('введите ОДНУ русскую букву: ').lower()
   if len(letter) != 1:
       continue

   if letter in secret_word:
       # brute force
       for i, symbol in enumerate(secret_word):  # (idx, item)
           if symbol == letter:
               gamer_word[i] = letter
       if '*' not in gamer_word:  # O(n)
           print('вы выиграли!!!')
           print('было загадано слово', secret_word.upper())
           break
   else:
       errors_counter += 1
       print('ошибок допущено:', errors_counter)
       if errors_counter == 8:
           print('вы проиграли ;(')
           break
   print(''.join(gamer_word))

print('возвращайтесь!')
