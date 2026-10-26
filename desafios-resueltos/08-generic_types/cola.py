class Cola:
    def __init__(self):
        self.__elementos = []

    def encolar(self, elemento):
        self.__elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.__elementos.pop(0)
        raise IndexError("La cola está vacía")

    def esta_vacia(self):
        return len(self.__elementos) == 0

    def __len__(self):
        return len(self.__elementos)


from collections import deque


class Queue:
    def __init__(self):
        self.__elementos = deque()

    def encolar(self, elemento):
        self.__elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.__elementos.popleft()
        raise IndexError("La cola está vacía")

    def esta_vacia(self):
        return len(self.__elementos) == 0


def main():
    c = Cola()
    c.encolar(5)
    c.encolar(6)
    print(c.desencolar())
    print(c.desencolar())


if __name__ == "__main__":
    main()
