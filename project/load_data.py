import psycopg2
import csv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def csv_exe(file_name, database):
    fd = open(file_name, 'r')
    sql_file = fd.read()
    fd.close()
    cursor = database.cursor()
    sqlComs = sql_file.split(';\n')
    sqlComs = list(filter(None, sqlComs))
    print(sqlComs)
    for com in sqlComs:
        cursor.execute(com)
        print(com)


database_postgres = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost",
                                     port="5432")
database_postgres.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
csv_exe('setup.sql', database_postgres)
database_postgres.close()

database_motor = psycopg2.connect(database="motordb", user="motordb", password="motordb", host="localhost", port="5432")
csv_exe('schema.sql', database_motor)

debug = False
if debug is False:
    ind_data = csv.reader(open('Motor_Vehicle_Crashes_-_Individual_Information__Three_Year_Window.csv'))
    motor_data = csv.reader(open('Motor_Vehicle_Crashes_-_Vehicle_Information__Three_Year_Window.csv'))
else:
    ind_data = csv.reader(open('test_case_i.csv'))
    motor_data = csv.reader(open('test_case_v.csv'))

next(ind_data)
next(motor_data)

cursor = database_motor.cursor()
print('Inserting motor data...')
for row in motor_data:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = None
        if row[i] == 'Not Applicable':
            row[i] = None
        if row[i] == 'Not Entered':
            row[i] = None
        if row[i] == 'None':
            row[i] = None
        if row[i] == 'Unknown':
            row[i] = None

    cursor.execute("INSERT INTO vehicle VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   [row[1], row[2], row[3], row[5], row[7], row[8], row[9], row[11], row[12], row[18]])
    cursor.execute("INSERT INTO cause VALUES (%s,%s,%s,%s,%s)",
                   [row[1], row[13], row[14], row[15], row[16]])

    cursor.execute("INSERT INTO event VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   [row[1], None, None, None, row[4], row[6], row[10], row[17], row[0]])
database_motor.commit()
print('Done inserting motor data...')

print('Inserting indv data...')
for row in ind_data:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = None
        if row[i] == 'Not Applicable':
            row[i] = None
        if row[i] == 'Not Entered':
            row[i] = None
        if row[i] == 'None':
            row[i] = None
        if row[i] == 'Unknown':
            row[i] = None

    cursor.execute("INSERT INTO victim VALUES (%s,%s,%s,%s,%s,%s)",
                   [row[1], row[2], row[4], row[7], row[8], row[14]])
    cursor.execute("INSERT INTO injury VALUES (%s,%s,%s,%s,%s)",
                   [row[1], row[3], row[11], row[12], row[13]])
    updated = cursor.execute("UPDATE event SET seating_pos = %s, ejection = %s, safety_equip =%s WHERE case_VID = %s",
                             [row[5], row[6], row[10], row[2]])
print('Done inserting indv data...')
database_motor.commit()

database_motor.close()


