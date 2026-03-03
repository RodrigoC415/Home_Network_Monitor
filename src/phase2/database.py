import psycopg2
from psycopg2 import sql
from datetime import datetime

class Database:
    def __init__(self, host="localhost", database="network_monitor", user="postgres", password="password"):
        try:
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            self.cur = self.conn.cursor()
            print("Connected to PostgreSQL database")
        except Exception as e:
            print("Error connecting to database:", e)
            raise

    def insert_metric(self, device_name, latency_ms, status):
        """Insert a ping metric into the metrics table"""
        try:
            query = sql.SQL(
                "INSERT INTO metrics (timestamp, device_name, latency_ms, status) VALUES (%s, %s, %s, %s)"
            )
            self.cur.execute(query, (datetime.now(), device_name, latency_ms, status))
            self.conn.commit()
        except Exception as e:
            print("Error inserting metric:", e)

    def close(self):
        """Close the database connection"""
        self.cur.close()
        self.conn.close()
        print("Database connection closed")