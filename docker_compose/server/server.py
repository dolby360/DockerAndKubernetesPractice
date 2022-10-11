import mysql.connector
import socket

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

while True:
    print("hellp")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    print("ssss")
    mydb = mysql.connector.connect(
        host="database",
        user="root",
        password="some_password",
        database="demo"
    )

    mycursor = mydb.cursor()
    print("here")
    mycursor.execute("SELECT * FROM Persons")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
