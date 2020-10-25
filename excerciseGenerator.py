import random

class ExerciseGen:
    def __init__(self, number):
        pass
    def gen1():
        template = """
        В одной из кодировок Unicode каждый символ кодируется {} битами. Вова написал текст (в нём нет лишних пробелов):
        «{}».
        Ученик вычеркнул из списка название одного из животных. Заодно он вычеркнул ставшие лишними запятые и пробелы — два пробела не должны идти подряд.
        При этом размер нового предложения в данной кодировке оказался на {} байт меньше, чем размер исходного предложения. Напишите в ответе вычеркнутое название животного."""
        templString = ""
        maxSymbols = random.randint(10, 25)
        encodingsSize = ['8', '16']
        encoding = random.choice(encodingsSize)
        if encoding == '16':
            numSymbols = [i for i in range(maxSymbols-5, maxSymbols+2) if i % 2 == 0]
        else:
            numSymbols = [i for i in range(maxSymbols - 5, maxSymbols + 2)]
        deletedBytes = random.choice(numSymbols)
        wordsInSentence = []
        print (template.format(encoding, '1 2 3', deletedBytes))
        for i in range(maxSymbols, maxSymbols-7, -1):
            with open("words_{}.txt".format(i), 'r', encoding='cp1251') as file:
                words = file.readlines()
                wordsNum = len(words)
                # wordIndex = random.
                word = random.choice(words).rstrip()
                # print (word)
                templString += word
                wordsInSentence.append(word)

                if i != maxSymbols - 6:
                    templString += ', '
                # print(file.__dir__())
                # random.randint()
        answer = int(deletedBytes)/(int(encoding)/8) - 2
        print (wordsInSentence, int(answer))
        print (template.format('156', templString, '15'))
    def sortWords():
            # file1 = open('word_{}_symbol'.format(str(i + 2)), 'w')
            words = {}
            with open ('zdf-win.txt', 'r', encoding = 'cp1251') as source:
                for i in source:
                    word = i.rstrip()
                    try:
                        words[len(word)] += [word]
                    except:
                        words[len(word)] = [word]
            for i in words:
                with open ('words_{}.txt'.format(str(i)), 'w') as file:
                    for word in words[i]:
                        file.write(word + '\n')
ExerciseGen.gen1()
# ExerciseGen.sortWords()