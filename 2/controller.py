from conexao import MongoConnect


class Controller():

    def save(self, name, author, genre):
        conexao = MongoConnect()
        music = {'name': name, 'author': author, 'genre': genre}
        conexao.save(music)
