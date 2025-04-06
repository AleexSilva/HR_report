import pandas as pd
import mysql.connector
from mysql.connector import Error
from decouple import config

# MySQL database connection configuration
db_config = {
    'user': config('user'),
    'password': config('password'),
    'host': config('host'),
    'database': config('database'),
}

# CSV file path
csv_file_path1 = '../data/Absenteeism_at_work.csv'
csv_file_path2 = '../data/compensation.csv'
csv_file_path3 = '../data/Reasons.csv'


# MySQL table name
table_name1 = 'Absenteeism'
table_name2 = 'Compensation'
table_name3 = 'Reasons'

# Read CSV file into a pandas DataFrame
df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)
df3 = pd.read_csv(csv_file_path3)

# column renaming

df1.columns=['ID','Reason_absence','Month_absence','Day_of_week','Seasons','Transportation_expense','Distance_from_Residence_to_Work','Service_time','Age','Work_load_AverageDay' ,'Hit_target','Disciplinary_failure','Education','Son','Social_drinker','Social_smoker','Pet','Weight','Height','Body_mass_index','Absenteeism_hours']

# Transform the DataFrame into a list of tuples
data1 = [tuple(x) for x in df1.to_records(index=False).tolist()]

# Transform the DataFrame into a list of tuples
data2 = [tuple(x) for x in df2.to_records(index=False).tolist()]

# Transform the DataFrame into a list of tuples
data3 = [tuple(x) for x in df3.to_records(index=False).tolist()]

#query

insert_query1 = f"""
                           INSERT INTO {table_name1} (
                               ID,Reason_absence,Month_absence,Day_of_week,Seasons,Transportation_expense,Distance_from_Residence_to_Work,Service_time,Age,Work_load_AverageDay,Hit_target,Disciplinary_failure,Education,Son,Social_drinker,Social_smoker,Pet,Weight,Height,Body_mass_index,Absenteeism_hours
                           )
                           VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                           """


insert_query2 = f"""
                           INSERT INTO {table_name2} (
                               ID,comp_hr
                           )
                           VALUES(%s, %s)
                           """
                           
                           
insert_query3 = f"""
                           INSERT INTO {table_name3} (
                               Number,Reason
                           )
                           VALUES(%s, %s)
                           """
                           
# Loadeing the first table -  Absenteeism_at_work
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.executemany(insert_query1,data1)
        if (len(data1) == cursor.rowcount):
            connection.commit()
            print("{} Row inserted".format(len(data1)))
        else:
            connection.rollback()
except Error as ex:
    print('Error during connection: {}'.format(ex))
finally:
    if connection.is_connected():
        connection.close()
        
        
# Loadeing the second table -  comapensation
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.executemany(insert_query2,data2)
        if (len(data2) == cursor.rowcount):
            connection.commit()
            print("{} Row inserted".format(len(data2)))
        else:
            connection.rollback()
except Error as ex:
    print('Error during connection: {}'.format(ex))
finally:
    if connection.is_connected():
        connection.close()
        
        
#Loading the second table - reasons
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.executemany(insert_query3,data3)
        if (len(data3) == cursor.rowcount):
            connection.commit()
            print("{} Row inserted".format(len(data3)))
        else:
            connection.rollback()
except Error as ex:
    print('Error during connection: {}'.format(ex))
finally:
    if connection.is_connected():
        connection.close()