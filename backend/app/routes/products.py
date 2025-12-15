from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_service import ProductService
from ..schemas.product import ProductResponse, ProductListResponse, ProductCreate
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/products",
    tags=["products"]
)

class AddToProductRequest(BaseModel):
    name: str
    description: str
    price: float
    category_id: int
    image_url: str

@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_category(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product_by_id(product_id)

@router.get("/category/{category_id}", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products_by_category(category_id)

@router.post("/add", status_code=status.HTTP_201_CREATED)
def create_product(request: AddToProductRequest, db: Session = Depends(get_db)):
    service = ProductService(db)
    item = ProductCreate(name=request.name, description=request.description, image_url=request.image_url, 
                         price=request.price, category_id=request.category_id)
    new_product = service.create_product(item)
    return {"product": new_product}

@router.delete("/delete/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    del_product = service.remove_product_by_id(product_id)
