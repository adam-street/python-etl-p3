create_schema =('''
  CREATE SCHEMA IF NOT EXISTS petl3
  ''')

create_table =('''
   CREATE TABLE IF NOT EXISTS petl3.viable_countys (
   geo_id INT NOT NULL,
   state TEXT NOT NULL,
   county TEXT NOT NULL,
   sales_vector INT NOT NULL);
     ''')

create_insert =('''
   INSERT INTO petl3.viable_countys
   VALUES (%s, %s, %s, %s);
   ''')
