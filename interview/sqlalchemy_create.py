from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

db_uri = 'sqlite:///db.sqlite3'
engine = create_engine(db_uri)


# Create a metadata instance
metadata = MetaData(engine)
# Declare a table
table = Table('GoblinCakeSales',metadata,
              Column('ID',Integer, primary_key=True),
              Column('Product',String),
              Column('Product_Type',String),
              Column('Price_Per',Integer),
              Column('Units_Sold',Integer),
              Column('Quarter',Integer))
# Create all tables
metadata.create_all()

engine.execute("""
insert into "GoblinCakeSales" (
		Product,
		Product_Type,
		Price_Per,
		Units_Sold,
		Quarter)
  Values
  ('Hobgoblin', 'Cake',4,388,1),
  ('Green Goblin', 'Cake',4,312,1),
  ('Forest Sprite', 'Canned Drink',0.8,97,1),
  ('Redcap', 'Cake',3.5,605,1),
  ('Imp', 'Cake',2,162,1),

  ('Hobgoblin', 'Cake',4,482,2),
  ('Green Goblin', 'Cake',4,312,2),
  ('Forest Sprite', 'Canned Drink',0.8,123,2),
  ('Redcap', 'Cake',4,401,2),
  ('Imp', 'Cake',1.5,540,2),
  ('Filthy Hobbit', 'Cookie',1,325,2),

  ('Hobgoblin', 'Cake',4,389,3),
  ('Green Goblin', 'Cake',4,302,3),
  ('Forest Sprite', 'Canned Drink',0.8,168,3),
  ('Redcap', 'Cake',4,433,3),
  ('Imp', 'Cake',2,486,3),
  ('Filthy Hobbit', 'Cookie',1,164,3),
  ('Wretched Elf', 'Cookie',1,212,3),
  ('Foul Dwarf', 'Cookie',1,168,3),
  ('Vile Human', 'Cookie',1,92,3),

  ('Hobgoblin', 'Cake',4,369,4),
  ('Green Goblin', 'Cake',4,333,4),
  ('Forest Sprite', 'Canned Drink',0.8,168,4),
  ('Redcap', 'Cake',4,462,4),
  ('Imp', 'Cake',2,501,4),
  ('Filthy Hobbit', 'Cookie',1,125,4),
  ('Wretched Elf', 'Cookie',1,201,4),
  ('Foul Dwarf', 'Cookie',1,162,4),
  ('Vile Human', 'Cookie',1,143,4),
  ('Wizard Spit', 'Hot Drink',3.5,455,4),
  ('Brownie', 'Cake',1.5,666,4)""")