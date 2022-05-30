#1.класс узел
class Uzel:
    # конструктор
    def __init__(self, sym, freq, left, right):
        self.freq = freq
        self.sym = sym
        self.left = left
        self.right = right
    def __repr__(self):
        return f"freq={self.freq}, sym={self.sym}, left={self.left}, right={self.right};"

#2.считка частот из файла и создание узлов
f=open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\encr.txt", "rb")
fic=sym = f.read(1).decode("ascii")  #считка фиктивных нулей
# print(ord(fic))
accum2=''#записываем частоту
str2=[]
accum1=''#записываем символ
sym=chr(2)
while sym!=chr(3):
    sym = f.read(1).decode("ascii")  #считка символа
    if sym == chr(3):
        break
    accum1 = sym  # считка символа
    sym = f.read(1).decode("ascii")  #считка символа
    while(sym!=chr(2)):
        accum2=accum2+sym
        sym=f.read(1).decode("ascii")
    #print(accum1, accum2)
    str2.append(Uzel(accum1, int(accum2), None, None))
    accum2 = ''
#3.сортировка списка узлов по частотам и построение дерева
#на место 0-го узла-новый добавляем в список, второй удаляем из списка
while(len(str2)>1):
    str2 = sorted(str2, key=lambda x: x.freq)# сортировка списка объектов по атрибуту: freq, создается lambda-функции, которая вернет freq объекта
    val1=str2[0]
    val2=str2[1]
    val=Uzel(-1, val1.freq+val2.freq, str2[0], str2[1])#присваиваем None-фиктивная вершина
    str2[0]=val
    str2.pop(1)
#4.рекурсивный обход дерева и создание словаря
dictionary={}#позволит хранить пары "ключ-значение", то есть будем хранить символы использованные в файле и в соответствие их кодировку в "0" и "1"
def Tree_traversal(str2, node):
    # str2=''#строка для хранения значений
    if (node.left is not None):
        Tree_traversal(str2+'0', node.left)
    if (node.right is not None):
        Tree_traversal(str2+'1', node.right)
    if (node.left is None and node.right is None):
        dictionary[str2]=node.sym
le=''
Tree_traversal(le, str2[0])
print(dictionary)
#5.основной цикл раскодирования
#открываем второй файл для записи в него значений
f1=open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\decr.txt", "w")
sym = f.read(1).decode("ascii")  # считка символа
print(len(sym))
i=1
str1=''
while len(sym)!= 0:
    ti=''.join(format(ord(sym), '08b'))#чтоб в двоичной просмотреть
    str1 += ti[i]
    i+=1
    if str1 in dictionary:#если нашли в словаре, то записываем в файл
        f1.write(dictionary[str1])
        str1 = ''
    if i==8:
        i = 1
        sym = f.read(1).decode("ascii")  # считка символа
        print(len(sym))
        if len(sym)==0:
            break
        if len(f.read(1).decode("ascii")) == 0:#до этого считали последний сивол
            print("=")
            ti = ''.join(format(ord(sym), '08b'))  # чтоб в двоичной просмотреть
            # if ord(fic)==0:
            #     break
            while i<8-ord(fic):
                str1 += ti[i]
                i+=1
                print(str1)
                if str1 in dictionary:  # если нашли в словаре, то записываем в файл
                    f1.write(dictionary[str1])
                    str1 = ''
            break
        f.seek(-1, 1)

f1.close()
f.close()
#СРАВНЕНИЕ ФАЙЛА ИСХОДНОГО С ДЕКОДИРУЕМЫМ
f1 = open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\new.txt", "r")
f2 = open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\decr.txt", "r")
sym1 = f1.read(1)
sym2 = f2.read(1)
while sym1!='':
    if sym1!=sym2:
        print("Файлы были разные. ")
        f1.close()
        f2.close()
        exit ()
    sym1 = f1.read(1)
    sym2 = f2.read(1)
if sym2!='':
    print("Файлы были разные ")
else:
    print("Файлы были одинаковые ")
# закрытие файлов
f1.close()
f2.close()