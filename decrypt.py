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
    accum2 = int(accum2)
    str2.append(Uzel(accum1, accum2, None, None))
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
#4.основной цикл раскодирования

f.close()