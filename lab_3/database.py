from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Змінні для збереження параметрів підключення до бази даних
DATABASE_URL = 'sqlite:///./test.db'

# Створення об'єкта для роботи з базою даних
engine = create_engine(DATABASE_URL)

# Створення об'єкта для визначення моделей бази даних
Base = declarative_base()

# Створення об'єкта для роботи з сесіями бази даних
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
