from controller import Controller

controller = Controller()

count = 0

while count < 3:
    name = str(input("Digite o nome da música: "))
    author = str(input("Digite o nome do autor: "))
    genre = str(input("Digite o nome da (gênero): "))
    count = count+1
    controller.save(name, author, genre)
    pass

