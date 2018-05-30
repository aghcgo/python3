# -*- coding: utf-8 -*-
import sys
import xlrd
import numpy
import pymysql
import traceback
#r = redis.Redis(host='127.0.0.1', port=6379,db=0)
#list=[]
book=xlrd.open_workbook('./hnhld/hnhld_hr201703.xls')
sheet=book.sheet_by_name('Sheet1')
print(sheet)
# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",passwd="zhg721019",db="hnhld_hr",charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS hnhld_hr.chnghld_hr201703")
 
# 使用预处理语句创建表
sql = """CREATE TABLE chnghld_hr201703(
  `number` int(11) NOT NULL,
  `unint_number` int(11) NOT NULL,
  `personnel_area` varchar(128) DEFAULT NULL,
  `secondary_institutions` varchar(64) DEFAULT NULL,
  `tertiary_institutions` varchar(64) DEFAULT NULL,
  `personnel_number` int(11) DEFAULT NULL,
  `name` varchar(16) DEFAULT NULL,
  `sex` varchar(16) DEFAULT NULL,
  `native_place` varchar(64) DEFAULT NULL,
  `nation` varchar(16) DEFAULT NULL,
  `date_birth` varchar(20) DEFAULT NULL,
  `work_time` varchar(20) DEFAULT NULL,
  `political_status` varchar(16) DEFAULT NULL,
  `political_status_time` varchar(20) DEFAULT NULL,
  `incumbent_post` varchar(64) DEFAULT NULL,
  `incumbent_post_time` varchar(20) DEFAULT NULL,
  `position_sequence` varchar(32) DEFAULT NULL,
  `duty_level` varchar(16) DEFAULT NULL,
  `duty_level_time` varchar(32) DEFAULT NULL,
  `technical_qualification` varchar(64) DEFAULT NULL,
  `technical_qualification_time` varchar(20) DEFAULT NULL,
  `professional_qualification` varchar(64) DEFAULT NULL,
  `professional_qualification_time` varchar(20) DEFAULT NULL,
  `fulltime_education` varchar(12) DEFAULT NULL,
  `fulltime_graduate_schools` varchar(64) DEFAULT NULL,
  `fulltime_professional` varchar(64) DEFAULT NULL,
  `fulltime_education_time` varchar(20) DEFAULT NULL,
  `Onthejob_education` varchar(12) DEFAULT NULL,
  `Onthejob_graduate_schools` varchar(64) DEFAULT NULL,
  `Onthejob_professional` varchar(64) DEFAULT NULL,
  `Onthejob_education_time` varchar(20) DEFAULT NULL,
  `localunint_time` varchar(20) DEFAULT NULL,
  `chng_time` varchar(20) DEFAULT NULL,
  `technical_skills` varchar(32) DEFAULT NULL,
  `technical_skills_duty_level` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
try:
	# 执行sql语句
	cursor.execute(sql)
	# 提交到数据库执行
	db.commit()
except Exception as e:
    # 如果发生错误则回滚
    db.rollback()
    traceback.print_exc()

for i in range(sheet.nrows):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql ="INSERT INTO hnhld_hr.chnghld_hr201703(number,unint_number,personnel_area,secondary_institutions,\
tertiary_institutions,personnel_number,name,sex,native_place,nation,date_birth,work_time,political_status,\
political_status_time,incumbent_post,incumbent_post_time,position_sequence,duty_level,duty_level_time,\
technical_qualification,technical_qualification_time,professional_qualification,professional_qualification_time,\
fulltime_education,fulltime_graduate_schools,fulltime_professional,fulltime_education_time,Onthejob_education,\
Onthejob_graduate_schools,Onthejob_professional,Onthejob_education_time,localunint_time,chng_time,technical_skills,\
technical_skills_duty_level) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (sheet.row_values(i)[0],\
sheet.row_values(i)[1],sheet.row_values(i)[2],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],\
sheet.row_values(i)[6],sheet.row_values(i)[7],sheet.row_values(i)[8],sheet.row_values(i)[9],sheet.row_values(i)[10],\
sheet.row_values(i)[11],sheet.row_values(i)[12],sheet.row_values(i)[13],sheet.row_values(i)[14],sheet.row_values(i)[15],\
sheet.row_values(i)[16],sheet.row_values(i)[17],sheet.row_values(i)[18],sheet.row_values(i)[19],sheet.row_values(i)[20],\
sheet.row_values(i)[21],sheet.row_values(i)[22],sheet.row_values(i)[23],sheet.row_values(i)[24],sheet.row_values(i)[25],\
sheet.row_values(i)[26],sheet.row_values(i)[27],sheet.row_values(i)[28],sheet.row_values(i)[29],sheet.row_values(i)[30],\
sheet.row_values(i)[31],sheet.row_values(i)[32],sheet.row_values(i)[33],sheet.row_values(i)[34])
    try:
	# 执行sql语句
        cursor.execute(sql)
   # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        print(i)
        print(sql)
        traceback.print_exc()
# 关闭数据库连接
# 关闭数据库连接
db.close()
print("good")
