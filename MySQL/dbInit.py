from configReader import REDIRECT_URL

tokens_query = "CREATE TABLE IF NOT EXISTS tokens (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, tgid BIGINT, access_token VARCHAR(256), refresh_token VARCHAR(256), expires_in INT, registration_at DATETIME)"
queue_query = "CREATE TABLE IF NOT EXISTS queue (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, tgid BIGINT, link VARCHAR(64), endtime INT)"

def initDb(db):
    db.execute(tokens_query)
    db.close_cursor()
    db.execute(queue_query)
    db.close_cursor()

    cursor = db.execute("SELECT COUNT(*) FROM queue")
    if cursor.fetchone()[0] == 0:
        for i in REDIRECT_URL:
            db.execute("INSERT INTO queue(link) VALUES (%s);", (str(i), ))
            db.close_cursor()