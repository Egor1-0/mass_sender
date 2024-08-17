import sqlite3
from typing import Any

class Database():
    def __init__(self) -> None:
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        

    def __call__(self) -> None:
        with self.connection:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS 'users' 
                (
                    user_id BIGINT NOT NULL PRIMARY KEY,
                    status BOOLEAN DEFAULT(TRUE)
                );
                  """
            )
            self.connection.commit()
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS `channels` 
                (
                    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user BIGINT NOT NULL,
                    channel_id BIGINT NOT NULL,
                    FOREIGN KEY (user) REFERENCES users (id)
                );

                """
            )
            self.connection.commit()


    def check_user(self, user_id: int) -> bool:
        with self.connection:
            return bool(self.cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,)).fetchone())


    def check_status(self, user_id: int) -> bool:
        with self.connection:
            return bool(self.cursor.execute("SELECT status FROM users WHERE user_id=?", (user_id,)).fetchone()[0])


    def set_status(self, user_id: int, status: bool) -> None:
        with self.connection:
            self.cursor.execute("UPDATE users SET status=? WHERE user_id=?", (status, user_id,))
            self.connection.commit()


    def add_user(self, user_id: int) -> None:
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id, ))
            self.connection.commit()


    def get_channels(self, channel_id: int) -> Any:
        with self.connection:
            return self.cursor.execute("SELECT channel_id FROM channels WHERE user=?", (channel_id,)).fetchall()
    

    def add_channel(self, user_id: int, channel_id: int) -> None:
        with self.connection:
            self.cursor.execute("INSERT INTO channels (user, channel_id) VALUES (?, ?)", (user_id, channel_id,))
            self.connection.commit()

db = Database()
db()
