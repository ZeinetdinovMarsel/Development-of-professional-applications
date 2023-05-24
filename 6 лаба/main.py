import cherrypy as cherrypy
from peewee import *

db = SqliteDatabase('database.db')


class MyTable(Model):
    class Meta:
        database = db
        db_table = 'lab6'

    idx = PrimaryKeyField(unique=True)
    date = DateField()
    cost = IntegerField()
    name = TextField()

    def Add(self, date, cost, name):
        MyTable(date=date, cost=cost, name=name).save()

    def Update(self, idx, date, cost, name):
        table = MyTable.get(idx=idx)
        table.date = date
        table.cost = cost
        table.name = name
        table.save()

    def getColumn(self):
        cursor = db.cursor()
        cursor.execute('PRAGMA table_info("lab6")')
        columns = [i[1] for i in cursor.fetchall()]
        return columns

    def getStrings(self):
        cursor = db.cursor()
        sqlite_select_query = """SELECT * from lab6"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        return result


class IndexPage(object):

    def __init__(self, columns, data):
        self.columns = columns
        self.data = data

    @cherrypy.expose
    def index(self):
        return f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>Terribly Bad Design</title>
                <style>
                    body {{
                        background-color: black;
                        font-family: Comic Sans MS, cursive, sans-serif;
                    }}
                    h1 {{
                        color: yellow;
                        font-size: 200px;
                        text-align: center;
                        text-shadow: -10px -10px 0 red, 10px -10px 0 red, -10px 10px 0 red, 10px 10px 0 red;
                        background-image: url("https://i.imgur.com/Xxj2d6c.jpg");
                        background-repeat: repeat;
                        background-blur: 10px;
                    }}
                    table {{
                        margin: auto;
                        max-width: 800px;
                        width: 80%;
                        border-collapse: separate;
                        border-spacing: 20px;
                        background-color: magenta;
                        transform: rotate(45deg);
                        opacity: 0.5;
                    }}
                    td, th {{
                        padding: 50px;
                        font-size: 50px;
                        border: 30px dotted yellow;
                        cursor: pointer;
                        border-radius: 100px;
                        box-shadow: inset 0px 0px 20px rgba(255, 0, 0, 0.75), 0px 0px 30px green, 0px 0px 50px blue;
                        text-shadow: none;
                    }}
                    th {{
                        background-color: green;
                        color: red;
                    }}
                    tr {{
                        transition: transform 10s ease-in-out, opacity 5s ease;
                    }}
                    tr:hover {{
                        transform: scale(5) rotate(-45deg);
                        opacity: 1;
                        background-color: yellow !important;
                    }}
                    td:hover {{
                        color: blue;
                        background-image: url("https://i.imgur.com/IrV8oD9.jpg");
                        background-repeat: repeat;
                        text-shadow: 0px 0px 30px white;
                    }}
                </style>
            </head>
            <body>
                <h1>BAD DESIGN</h1>
                <table>
                    <tr>
                        {
        "".join(["<th>" + i + "</th>"
                 for i in self.columns])
        }
                    </tr>
                    {self.data}
                </table>
            </body>
        </html>
        '''


def table_style(strings):
    table_line = ""
    for tr in strings:
        table_line += "<tr>"
        for td in tr:
            table_line += f"<td style='padding: 10px; text-align:center; font-size: 15px;" \
                          f" border: 1px solid #ddd;'> {td} </td>"
        table_line += "</tr>"
    return table_line


if __name__ == '__main__':
    table = MyTable()
    # table.Add("19.05.2023 16:56:00", 1656, "lab6test")
    # table.Update(5, "31.12.2023 23:59:59", 9999, "santas stick")

    columns = table.getColumn()
    lines = table.getStrings()

    table_line = table_style(lines)

    cherrypy.quickstart(IndexPage(columns, table_line))

    db.close()
