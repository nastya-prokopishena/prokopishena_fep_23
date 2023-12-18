from pydantic import BaseModel


class ShipBase(BaseModel):
    destination_port_id: int
    total_weight_capacity: int
    fuel_consumption_per_km: float
    container_ids: str
    type: str


class ShipCreate(ShipBase):
    pass


class Ship(ShipBase):
    ship_id: int

    class Config:
        orm_mode = True


class PortBase(BaseModel):
    latitude: float
    longitude: float
    container_ids: str


class PortCreate(PortBase):
    pass


class Port(PortBase):
    port_id: int

    class Config:
        orm_mode = True


class ContainerBase(BaseModel):
    weight: int
    type: str
    item_ids: str


class ContainerCreate(ContainerBase):
    pass


class Container(ContainerBase):
    container_id: int

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    weight: float
    count: int
    container_id: int
    type: str
    specific_attribute: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    item_id: int

    class Config:
        orm_mode = True
