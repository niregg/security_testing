import sqlite3

def login_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # PERINGATAN: Ini adalah contoh kode rentan (SQL Injection) untuk pengujian SAST SonarQube
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        print("Login Berhasil!")
    else:
        print("Login Gagal!")
        
    conn.close()