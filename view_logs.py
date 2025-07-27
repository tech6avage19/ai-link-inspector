import sqlite3

conn = sqlite3.connect("link_inspector.db")
c = conn.cursor()
c.execute("SELECT url, is_suspicious, pattern, scanned_at FROM scans ORDER BY scanned_at DESC")

for row in c.fetchall():
    url, suspicious, pattern, timestamp = row
    status = "❌ Bad" if suspicious else "✅ Good"
    print(f"[{timestamp}] {status} — {url} (pattern: {pattern})")

conn.close()
