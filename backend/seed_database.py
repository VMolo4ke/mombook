import os
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime, ForeignKey, event
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime, timezone
from contextlib import contextmanager

# --- Конфигурация Базы Данных ---
# Имя файла базы данных (будет создан в той же папке, что и этот скрипт)
DATABASE_URL = "sqlite:///./shop.db"

# Создаем базовый класс для декларативного стиля
Base = declarative_base()

# --- Определение Моделей (на основе вашего кода) ---

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url = Column(String)
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))

    category = relationship("Category", back_populates="products")

# --- Функция Заполнения Данными ---

def seed_data(db_session):
    """Добавляет тестовые категории и продукты в базу данных."""
    print("Начало заполнения базы данных тестовыми данными...")

    # 1. Создаем категории
    category_electronics = Category(name="Электроника", slug="electronics")
    category_books = Category(name="Книги", slug="books")
    category_clothing = Category(name="Одежда", slug="clothing")

    # Добавляем категории в сессию, чтобы получить их ID автоматически при коммите
    db_session.add_all([category_electronics, category_books, category_clothing])
    db_session.commit()
    print("Категории добавлены.")

    # 2. Создаем продукты и связываем их с категориями
    products_list = [
        # Электроника (3 товара)
        Product(
            name="Ноутбук Dell XPS 13",
            description="Мощный и легкий ноутбук с безрамочным дисплеем.",
            price=120000.00,
            category=category_electronics,
            image_url="http://example.com/images/laptop.jpg"
        ),
        Product(
            name="Смартфон iPhone 14",
            description="Последняя модель смартфона от Apple.",
            price=85000.00,
            category=category_electronics,
            image_url="http://example.com/images/iphone14.jpg"
        ),
        Product(
            name="Беспроводные наушники Sony",
            description="Наушники с шумоподавлением и отличным звуком.",
            price=22000.00,
            category=category_electronics,
            image_url="http://example.com/images/headphones.jpg"
        ),

        # Книги (2 товара)
        Product(
            name="1984",
            description="Классический антиутопический роман Джорджа Оруэлла.",
            price=750.00,
            category=category_books,
            image_url="http://example.com/images/1984.jpg"
        ),
        Product(
            name="Мастер и Маргарита",
            description="Культовый роман Михаила Булгакова.",
            price=600.00,
            category=category_books,
            image_url="http://example.com/images/master.jpg"
        ),

        # Одежда (2 товара)
        Product(
            name="Футболка хлопок M",
            description="Базовая белая футболка из 100% хлопка.",
            price=1200.00,
            category=category_clothing,
            image_url="http://example.com/images/tshirt.jpg"
        ),
        Product(
            name="Джинсы прямые синие",
            description="Классические мужские джинсы.",
            price=4500.00,
            category=category_clothing,
            image_url="http://example.com/images/jeans.jpg"
        ),
    ]

    db_session.add_all(products_list)
    db_session.commit()
    print("Продукты добавлены.")
    print("База данных успешно заполнена!")


# --- Основное выполнение скрипта ---

if __name__ == "__main__":
    # Создаем движок БД
    engine = create_engine(DATABASE_URL)

    # Создаем все таблицы, если их еще нет
    Base.metadata.create_all(bind=engine)
    print(f"Убедились, что таблицы существуют в файле: {DATABASE_URL.split('///./')[1]}")

    # Создаем фабрику сессий
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Используем контекстный менеджер для безопасной работы с сессией
    try:
        db = SessionLocal()
        # Проверяем, пустая ли таблица категорий перед заполнением
        if db.query(Category).count() == 0:
            seed_data(db)
        else:
            print("База данных уже содержит категории. Пропускаю заполнение.")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        if 'db' in locals() and db:
            db.rollback()
    finally:
        if 'db' in locals() and db:
            db.close()
