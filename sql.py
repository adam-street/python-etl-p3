insert_data = ('''
    INSERT INTO p3_etl.viable_countys
    VALUES (%s, %s, %s, %s);
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS p3_etl;
    
    DROP TABLE IF EXISTS p3_etl.viable_countys;
    
    CREATE TABLE IF NOT EXISTS p3_etl.viable_countys (
        geo_id INT,
        state TEXT,
        county TEXT,
        sales_vector INT
        );        
''')
