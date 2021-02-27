stroka=str(input('Введите исходные данные '))

stroka.split()

print('Исходные данные:\t'+str(stroka))

print("\n\nВведите слово для поиска:")
SearchWord = str(input())

pozcount = 0
negcount = 0
flag = 0
wordcount = 0
result = ''

print("\n\n")

for i in range(len(stroka)):
  if stroka[i] != ' ' and flag == 0:
    wordcount += 1
    flag = 1
  else:
    if stroka[i] == ' ':
      flag = 0
print("\n\nКоличество слов в строке:" + str(wordcount))

print("\n\n")


for word in stroka.split():
  if word == SearchWord:
    print(str(word) + " соответсвует")
    result = word
    pozcount += 1
  else:
    print(str(word) + " не соответсвует ")
    negcount += 1
if negcount == wordcount:
  print("\n\nТакого слова в строке нет!!!")
else:
  print("\n\nКоличество не соответсвующих слов в строке:\t" + str(negcount))
  print("Количество соответсвующих слов в строке:\t" + str(pozcount) + " - " + str(result))