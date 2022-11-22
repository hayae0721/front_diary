from sqlalchemy import create_engine

import pymysql

pymysql.install_as_MySQLdb()

DATABASES = create_engine('mariadb+mysqldb://root:1234@localhost:3306/urop', echo=True)