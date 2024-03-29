import pymysql
from model.project import Project


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_project_list(self):

        sheet = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, name, description FROM mantis_project_table")
            for row in cursor:
                (id, name, description) = row
                sheet.append(Project(id=id, name=name, description=description))
        finally:
            cursor.close()
        return sheet