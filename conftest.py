import pytest
import time

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from backend.models import Product, ProductPhotobase, Shop
from users.models import CustomUser


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    #driver.maximize_window()
    yield driver
    #time.sleep(20)
    driver.quit()


@pytest.fixture()
def setup_products():

    user = CustomUser.objects.create(
        username='mufasa',
        phone='89130370453',
        photo=r'C:\Users\msi rgb\Desktop\А\dospeh.jpg',
    )

    shop = Shop.objects.create(
        name="Магазин 1",
        description='Описание 1',
        avatar=r'C:\Users\msi rgb\Desktop\А\dospeh.jpg',
        header=r'C:\Users\msi rgb\Desktop\А\dospeh.jpg',
        owner=user,
    )

    photobase1 = ProductPhotobase.objects.create(
        image1=r'C:\Users\msi rgb\Desktop\А\dospeh.jpg',
        image2='',
        image3='',
        image4='',
        image5='',
        image6='',
        image7='',
        image8='',
        image9='',
        image10='',
    )

    photobase2 = ProductPhotobase.objects.create(
        image1=r'C:\Users\msi rgb\Desktop\А\dospeh.jpg',
        image2='',
        image3='',
        image4='',
        image5='',
        image6='',
        image7='',
        image8='',
        image9='',
        image10='',
    )

    # Создаем несколько тестовых товаров
    Product.objects.create(
        name="Товар 1",
        description="Описание товара 1",
        price=128,
        quantity=100,
        weight=100,
        date_manufacture=datetime.now(),
        photobase=photobase1,
        shop=shop,
    )
    Product.objects.create(
        name="Товар 2",
        description="Описание товара 2",
        price=20,
        quantity=50,
        weight=50,
        date_manufacture=datetime.now(),
        photobase=photobase2,
        shop=shop,
    )

