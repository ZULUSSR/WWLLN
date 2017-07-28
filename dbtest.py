import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS TEST(year INT , month INT, day INT, hours INT, minutes INT, seconds REAL, value1 REAL, value2 REAL, value3 REAL, num INT)')

def dynamic_data_entry(values):
        c.execute("INSERT INTO TEST VALUES(?,?,?,?,?,?,?,?,?,?)", values)
        
        
create_table()
inputfile = "test.txt"
fin = open(inputfile, mode = 'r', encoding = 'ascii')
isreal = False
value = ''
values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
values.clear()
for line in fin:
        for i in line:
                if i == '.':
                        isreal = True
                if i != ' ' and i != '\n':
                        value += i
                        continue
                if value != '':
                        if isreal == True:
                                value = float(value)
                        else:
                                value = int(value)
                        isreal = False
                        values.append(value)
                        value = ''
                else:
                        continue
        dynamic_data_entry(values)         
        values.clear()
c.close()
conn.commit()
conn.close()
