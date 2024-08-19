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
                    end_time_subscription INTEGER DEFAULT(0)
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
                    channel_name VARCHAR(200) NOT NULL,
                    channel_id BIGINT NOT NULL,
                    status BOOLEAN DEFAULT(TRUE),
                    FOREIGN KEY (user) REFERENCES users (id)
                );
                """
            )
            self.connection.commit()


    def check_user(self, user_id: int) -> bool:
        with self.connection:
            return bool(self.cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,)).fetchone())


    def check_user_status(self, user_id: int):
        with self.connection:
            return self.cursor.execute("SELECT end_time_subscription FROM users WHERE user_id=?", (user_id,)).fetchone()


    def set_user_status(self, user_id: int, end_time_subscription: bool) -> None:
        with self.connection:
            self.cursor.execute("UPDATE users SET end_time_subscription=? WHERE user_id=?", (end_time_subscription, user_id,))
            self.connection.commit()


    def add_user(self, user_id: int) -> None:
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id, ))
            self.connection.commit()


    def get_channels(self, user_id: int):
        with self.connection:
            return self.cursor.execute("SELECT channel_id, status, channel_name FROM channels WHERE user=?", (user_id,)).fetchall()
    

    def add_channel(self, user_id: int, channel_id: int, channel_name: str) -> None:
        with self.connection:
            self.cursor.execute("INSERT INTO channels (user, channel_id, channel_name) VALUES (?, ?, ?)", (user_id, channel_id, channel_name,))
            self.connection.commit()
            
    
    def delete_channel(self, channel_id: int) -> None:
        with self.connection:
            self.cursor.execute("DELETE FROM channels WHERE channel_id=?", (channel_id,))
            self.connection.commit()


db = Database()
db()
