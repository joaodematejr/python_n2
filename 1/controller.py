import psycopg2
from db import Connection


class Controller():

    def save(self, author, tipo, genre):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = """INSERT INTO music (name, author, genre) values ('{0}', '{1}', '{2}');""".format(author, tipo, genre)
            cursor.execute(insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
