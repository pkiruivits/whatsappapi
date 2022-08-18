from typing import List, Optional

from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    location: str
    applications: Optional[str] = None
    characteristics: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ProductFileBase(BaseModel):
    fileurl: str
    product_id:int


class ProductFileCreate(ProductFileBase):
    pass


class ProductFile(ProductFileBase):
    id: int
    #is_active: bool
    #items: List[Item] = []

    class Config:
        orm_mode = True

class ProductImageBase(BaseModel):
    Imageurl: str
    product_id:int


class ProductImageCreate(ProductImageBase):
    pass


class ProductImage(ProductImageBase):
    id: int
    #is_active: bool
    #items: List[Item] = []

    class Config:
        orm_mode = True