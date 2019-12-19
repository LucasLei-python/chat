import pymysql


class Mysql:
    def __init__(self, user="root", password="123456", database="stu"):
        self.__host = '176.140.10.103'
        self.__port = 3306
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = 'utf8'
        self.__connect()

    def __connect(self):
        self.__db = pymysql.connect(host=self.__host, port=self.__port,
                                    user=self.__user,
                                    password=self.__password,
                                    database=self.__database,
                                    charset=self.__charset)

    # 查询
    def query(self, sql, list_paramers=None, size=None):
        """
        ex:sql=select *from test where id=%s
           list_paramenrs=[15]
        :param sql: 需执行的sql语句
        :param list_paramers: 参数集合，可不传
        :return: 成功返回元祖结果或空，否则返回失败以及失败原因
        """
        self.__cur = self.__db.cursor()
        try:
            self.__cur.execute(sql, list_paramers)
            if size:
                return self.__cur.fetchmany(size=size)
            return self.__cur.fetchall()
        except Exception as e:
            return "查询失败：" + str(e)

    # 增、删、改
    def in_up_de(self, sql, list_paramers=None, ):
        """
            单笔增、删、改方法
        :param sql:
        :param list_paramers: 参数集合，可不传
        :return: 成功返回操作成功，失败返回操作失败
        """
        self.__cur = self.__db.cursor()
        try:
            self.__cur.execute(sql, list_paramers)
            self.__db.commit()
            return "操作成功"
        except Exception as e:
            self.__db.rollback()
            return "操作失败：" + str(e)

    # 批量多次增、删、改不同语句类型
    def batch_in_up_de(self, sql_list):
        """
        ex:my01.batch_in_up_de([["update person set id=%s where id=%s",
                         [(10, 1), (20, 2)]],["delete from person where id=%s",
                                              [1, 2]]])
        :param sql_list: 同一类型语句的二维列表，
        :return: 成功返回操作成功，失败返回操作失败
        """
        self.__cur = self.__db.cursor()
        try:
            for sql in sql_list:
                self.__cur.executemany(sql[0], sql[1])
            self.__db.commit()
            return "操作成功"
        except Exception as e:
            self.__db.rollback()
            return "操作失败：" + str(e)

    def close(self):
        if hasattr(self, "__cur"):
            self.__cur.close()
        if hasattr(self, "__db"):
            self.__db.close()
