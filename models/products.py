from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_app.database import Base

class ProductFiles(Base):
    __tablename__ = "ProductFiles"

    id = Column(Integer, primary_key=True, index=True)
    product_Id = Column(Integer, ForeignKey("Products.id"))
    fileUrl = Column(String)

    productfl = relationship("products", back_populates="product_files")

class ProductImages(Base):
    __tablename__ = "ProductImages"

    id = Column(Integer, primary_key=True, index=True)
    product_Id = Column(Integer, ForeignKey("Products.id"))
    ImageUrl = Column(String)

    productimg = relationship("products", back_populates="product_images")

class Products(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    location = Column(String, null=True)

    product_images = relationship("ProductImages", back_populates="productimg")
    product_files = relationship("ProductFiles", back_populates="productfl")
