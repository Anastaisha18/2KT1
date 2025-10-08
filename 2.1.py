# Класс для узла дерева Хаффмана
class Node:
    def __init__(self, char, freq):
        self.char = char  # Символ (None для внутренних узлов)
        self.freq = freq  # Частота символа или сумма частот потомков
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок

class HuffmanTree:
    def __init__(self, root):
        self.root = root  # Корневой узел дерева

    def print_tree(self):
        self.print_codes(self.root, '')  # Печать кодов Хаффмана

    def print_codes(self, node, code):
        if node is None:
            return
        if node.char is not None:
            print(f"'{node.char}': {code}")  # Печать символа и его кода
        self.print_codes(node.left, code + '0')  # Рекурсивный обход левого поддерева
        self.print_codes(node.right, code + '1')  # Рекурсивный обход правого поддерева

    def print_tre(self, node, h):
        if node:
            self.print_tre(node.right, h+1)  # Рекурсивный обход правого поддерева
            for i in range(1, h+1):
                print('    ', end='')  # Добавление отступов для визуализации уровня
            if node.char is not None:
                print(f"'{node.char}':{node.freq}")  # Печать листового узла
            else:
                print(node.freq)  # Печать внутреннего узла
            self.print_tre(node.left, h+1)  # Рекурсивный обход левого поддерева

def build_huffman_tree(text):
    freq = {}  # Словарь для подсчета частот символов
    for char in text:
        if char != ' ':  # Игнорирование пробелов
            freq[char] = freq.get(char, 0) + 1  # Увеличение счетчика частоты

    nodes = []  # Список для хранения узлов
    for char, count in freq.items():
        nodes.append(Node(char, count))  # Создание узлов для каждого символа

    while len(nodes) > 1:  # Пока не останется один узел (корень)
        for i in range(len(nodes)):
            for j in range(len(nodes) - 1):
                if nodes[j].freq > nodes[j + 1].freq:
                    nodes[j], nodes[j + 1] = nodes[j + 1], nodes[j]  # Сортировка пузырьком

        left = nodes.pop(0)  # Извлечение узла с наименьшей частотой
        right = nodes.pop(0)  # Извлечение узла со следующей наименьшей частотой
        parent = Node(None, left.freq + right.freq)  # Создание родительского узла
        parent.left = left  # Установка левого потомка
        parent.right = right  # Установка правого потомка
        nodes.append(parent)  # Добавление родительского узла обратно в список

    return HuffmanTree(nodes[0]) if nodes else HuffmanTree(None)  # Создание дерева с корневым узлом

text = input("Введите текст: ")  # Ввод текста от пользователя
huffman_tree = build_huffman_tree(text)  # Построение дерева Хаффмана
huffman_tree.print_tree()
huffman_tree.print_tre(huffman_tree.root, 0)  # Вывод дерева в консоли
