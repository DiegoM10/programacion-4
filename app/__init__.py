import pymysql
db = pymysql.connect("localhost","root","root123","test")
cursor =  db.cursor()
#cursor.execute("SELCET VERSION()")
#data = cursor.fetchone()
#print("version de mariaDb: %s"%data)


#cursor.execute("DROP TABLE IF EXISTS EMPLEADO")
#sql= """CREATE TABLE EMPLEADO(
#NOMBRE VARCHAR(20) NOT NULL,
#APELIDO VARCHAR(20),
#EDAD INT,
#SEXO CHAR(1),
#SALARIO FLOAT
#)"""
#cursor.execute(sql)
sql = """INSERT INTO EMPLEADO(NOMBRE,APELLIDO,EDAD,SEXO,SALARIO)
        VALUES('Petra','Petrov',88,'F', 15000)"""
try:
     cursor.execute(sql)
     db.commit()
except:
       db.rollback()
       print("error")
db.close()


#e = int(input("Edad de petra> "))
#salarios = []
#sql = "SELECT * FROM EMPLEADO WHERE EDAD > '%d' " %e
#try:
#   cursor.execute(sql)
 #  resultados = cursor.fetchall()
  # for registro in resultados:
  #     salarios = registro[4]
   #    salarios.append(salarios)
#except:
 #   print("error al obtener datos!")
#db.close()
#print("Elsalaario mas altode petra fue de $%d"+ str(max(salarios)))

# Actualizar datos
#sql = "UPDATE EMPLEADO SET EDAD = EDAD + 1 WHERE SEXO = 'F'"
#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()
#db.close()

# Borrar datos
#sql = "DELETE FROM EMPLEADO WHERE EDAD < 18"
#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()
#db.close()