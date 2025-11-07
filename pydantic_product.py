from pydantic import BaseModel, Field

class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше 0")
    tags: list[str] = []
    market: Market

class Box(BaseModel):
    dick: str
    size: int

product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"],
    "market": {
            "id": 1,
            "name": "Amazon"
        },
    "dick": "xren",
    "size": 56
}

product = Product(**product_data)
print(product)

print('\n')
box = Box(**product_data)
print(box)
