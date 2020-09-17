import sqlite3
from faker import Faker
import pandas as pd
# from urllib import parse
# from pymongo import MongoClient
# import pymysql


class CreateData(object):
    def __init__(self):
        # 选择中文
        fake = Faker('zh_CN')
        # 生成数据改变循环体来控制数据量rang(?)
        self.data_total = [[fake.name(),
                            fake.job(),
                            fake.company(),
                            fake.phone_number(),
                            fake.company_email(),
                            fake.address(),
                            fake.date_time(tzinfo=None),
                            fake.country(),
                            fake.password()] for x in range(100)]
        print(self.data_total)

    # 写入excel
    def deal_excel(self):
        df = pd.DataFrame(
            self.data_total,
            columns=[
                'name',
                'job',
                'company',
                'phone_number',
                'company_email',
                'address',
                'date_time',
                'country',
                'password'])
        # 保存到本地excel
        df.to_excel("data_total.xlsx", index=False)
        print("Processing completed to excel")

    # 写入txt
    def deal_txt(self):
        with open('data_total.txt', 'w', errors='ignore', encoding='utf-8') as output:
            output.write(
                'name,job,company,phone_number,company_email,address,date_time,country\n')
            for row in self.data_total:
                rowtxt = '{},{},{},{}'.format(row[0], row[1], row[2], row[3])
                output.write(rowtxt)
                output.write('\n')
            output.close()
        print("Processing completed to txt")

    # # 写入mongodb
    # def deal_mongodb(self):
    #     port = 27017
    #     host = 'localhost'
    #     user_name = 'root'
    #     db_name = 'data'
    #     passwd = 'root'
    #     passwd = parse.quote(passwd)
    #     mango_uri = 'mongodb://%s:%s@%s:%s/%s' % (user_name, passwd, host, port, db_name)  # 链接时需要指定数据库
    #     conn = MongoClient(mango_uri)  # 创建链接
    #     db = conn[db_name]  # 连接coder数据库
    #     mongodata = db['data_total']
    #     for val in self.data_total:
    #         mongodata.insert(
    #             {"name": val[0], 'job': val[1], 'company': val[2], 'phone_number': val[3], "company_email": val[4],
    #              'address': val[5], 'date_time': val[6]})
    #     print("Processing completed to mongodb")

    # # 写入mysql
    # def deal_mysql(self):
    #     # 打开数据库连接
    #     db = pymysql.connect("localhost", "root", "root", "test2")
    #     # 使用cursor()方法获取操作游标
    #     cursor = db.cursor()
    #     # SQL 插入语句
    #     for val in self.data_total:
    #         sql = "insert into data_total(name,job,company,phone_number,company_email,address,date_time)value ('%s','%s','%s','%s','%s','%s','%s')" % (
    #             val[0], val[1], val[2], val[3], val[4], val[5], val[6])
    #         try:
    #             # 执行sql语句
    #             cursor.execute(sql)
    #             # 执行sql语句
    #             db.commit()
    #             print("insert ok")
    #         except:
    #             # 发生错误时回滚
    #             db.rollback()
    #         # 关闭数据库连接

    # 写入sqlite3

    def deal_sqlite(self):
        # 打开数据库连接
        conn = sqlite3.connect('data_total.db')
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS data_total(name,job,company,phone_number,company_email,address,date_time,country)")
        # SQL 插入语句
        for val in self.data_total:
            sql = "insert into data_total(name,job,company,phone_number,company_email,address,date_time,country) value('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7])
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                conn.commit()
                print("insert ok")
            except BaseException:
                # 发生错误时回滚
                conn.rollback()
                print("发生错误时回滚")
        # 关闭数据库连接
        conn.close()


if __name__ == '__main__':
    data = CreateData()
    data.deal_excel()
    data.deal_txt()
    # data.deal_mongodb()
    # data.deal_mysql()
    data.deal_sqlite()
