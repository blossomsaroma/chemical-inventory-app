#!/usr/bin/env python3
from app.database import engine
import sqlalchemy as sa

def check_database():
    with engine.connect() as conn:
        # Check what tables exist
        result = conn.execute(sa.text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = [row[0] for row in result]
        print("Tables in database:", tables)
        
        # Check users table structure if it exists
        if 'users' in tables:
            result = conn.execute(sa.text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users' ORDER BY ordinal_position"))
            columns = [(row[0], row[1]) for row in result]
            print("\nUsers table columns:")
            for col_name, col_type in columns:
                print(f"  - {col_name}: {col_type}")

if __name__ == "__main__":
    check_database() 