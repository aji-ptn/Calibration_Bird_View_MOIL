import mysql.connector

mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6507609",
    password="R3AyNcpMrq",
    database="sql6507609"
)

mycursor = mydb.cursor(buffered=True)

# create table
# sql = "CREATE TABLE cam_parameters (camera_name VARCHAR(255), camera_fov INT(255), sensor_width FLOAT, sensor_height " \
#       "FLOAT, icx INT, icy INT, ratio FLOAT, image_width INT, image_height INT, calibration_ratio FLOAT, parameter_0 " \
#       "DOUBLE, parameter_1 DOUBLE, parameter_2 DOUBLE, parameter_3 DOUBLE, parameter_4 DOUBLE, parameter_5 DOUBLE) "
# mycursor.execute(sql)

# insert new parameter
sql = "INSERT INTO cam_parameters (camera_name, camera_fov, sensor_width, sensor_height, icx, icy, ratio,image_width, image_height, calibration_ratio, parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5 " \
      ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

val = ('narl_fisheye', '220', '1.4', '1.4', 2025, 1525, 1, 4000, 3000, 6.25, 0, 0, 0, -3.48, 2.48, 121.8)
mycursor.execute(sql, val)

# sql = "DELETE FROM cam_parameters WHERE camera_name='entaniya_vr220_2_2592x1944'"

mydb.commit()


# sql = "UPDATE cam_parameters SET camera_name ='Intel-T265-L' WHERE camera_name ='Intel-T265'"
#
# mycursor.execute(sql)
# mydb.commit()

# sql = "SELECT * FROM cam_parameters"
# mycursor.execute(sql)
# mydb.commit()
# myresult = mycursor.fetchall()
# print(myresult)

# for x in myresult:
#   print(x)
  # a = list(x)
  # print(type(a[5]))

# mycursor.execute("CREATE DATABASE data_parameter")
# print("%" %25)