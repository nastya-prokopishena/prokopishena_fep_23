from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ship(Base):
    __tablename__ = "ships"
    ship_id = Column(Integer, primary_key=True, index=True)
    destination_port_id = Column(Integer, ForeignKey("ports.port_id"))
    total_weight_capacity = Column(Integer)
    fuel_consumption_per_km = Column(Float)
    container_ids = Column(String)
    type = Column(String)
    port = relationship("Port", back_populates="ships")


class Port(Base):
    __tablename__ = "ports"
    port_id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    container_ids = Column(String)
    ships = relationship("Ship", back_populates="port")


class Container(Base):
    __tablename__ = "containers"
    container_id = Column(Integer, primary_key=True, index=True)
    weight = Column(Integer)
    type = Column(String)
    item_ids = Column(String)


class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float)
    count = Column(Integer)
    container_id = Column(Integer, ForeignKey("containers.container_id"))
    type = Column(String)
    specific_attribute = Column(String)
    container = relationship("Container", back_populates="items")
