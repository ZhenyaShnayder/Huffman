# 1.подсчет частот
# создание псевдо-ассоциативного массива
frequencies=[0 for i in range (256)]
f=open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\new.txt", "r")
sym=f.read(1)
frequencies[ord(sym)] +=1
while sym!='':
    frequencies[ord(sym)] +=1
    sym=f.read(1)
f.close()
# 2.класс Uzel
class Uzel:
    #конструктор
    def __init__(self,ascii_code, freq, left, right):
        self.freq=freq
        self.ascii_code=ascii_code
        self.left=left
        self.right=right
    def __repr__(self):
        return f"freq={self.freq}, ascii_code={self.ascii_code}, left={self.left}, right={self.right};"
#3.список узлов
str2=[]
str3 = str2.copy()
for i in range (256):
    if frequencies[i]!=0:
        #создание узла
        str2.append(Uzel(i, frequencies[i], None, None))
#4.сортировка списка узлов по частотам и построение дерева
#на место 0-го узла-новый добавляем в список, второй удаляем из списка
while(len(str2)>1):
    str2 = sorted(str2, key=lambda x: x.freq)# сортировка списка объектов по атрибуту: freq, создается lambda-функции, которая вернет freq объекта
    val1=str2[0]
    val2=str2[1]
    val=Uzel(-1,val1.freq+val2.freq,str2[0],str2[1])#присваиваем None-фиктивная вершина
    str2[0]=val
    str2.pop(1)
#5.рекурсивный обход дерева и создание словаря
dictionary={}#позволит хранить пары "ключ-значение", то есть будем хранить символы использованные в файле и в соответствие их кодировку в "0" и "1"
def Tree_traversal(str2, node):
    # str2=''#строка для хранения значений
    if (node.left is not None):
        Tree_traversal(str2+'0', node.left)
    if (node.right is not None):
        Tree_traversal(str2+'1', node.right)
    print(str2)
    if (node.left is None and node.right is None):
        dictionary[chr(node.ascii_code)]=str2
    print(dictionary)
le=''
Tree_traversal(le, str2[0])
# print(dictionary)










#f.write(chr(13).encode("ascii"))
# f.write(chr(10).encode("ascii"))
# f=open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\new.txt", "r")
# sym=f.read(1)