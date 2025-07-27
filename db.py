# db.py
import sqlite3

DB_NAME = "link_inspector.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            is_suspicious INTEGER NOT NULL,
            pattern TEXT,
            scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_scan(url, is_suspicious, pattern):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO scans (url, is_suspicious, pattern)
        VALUES (?, ?, ?)
    ''', (url, int(is_suspicious), pattern))
    conn.commit()
    conn.close()
