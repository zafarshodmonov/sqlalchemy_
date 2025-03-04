from sqlalchemy import create_engine, text, URL
from config_data import DATABASE_URL

# Create Engine
engine = create_engine(DATABASE_URL)

# Test Connection
with engine.connect() as connection:

    data = connection.execute(text("""SELECT * FROM employees;"""))
    rows = data.fetchmany(10)
    
    
    for row in rows:
        ID = row.id 
        name = row.name 
        manager_id = row.manager_id
        print(f"ID: {ID}, Name: {name}, Manager ID: {manager_id}")
        
    # Print Connection
    print("Connected to the database successfully!")
