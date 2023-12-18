from sqlalchemy.orm import Session
import models


def create_ship(db: Session, ship: models.Ship):
    db_ship = models.Ship(**ship.dict())
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship


def get_ships(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ship).offset(skip).limit(limit).all()


def get_ship(db: Session, ship_id: int):
    return db.query(models.Ship).filter(models.Ship.ship_id == ship_id).first()


def update_ship(db: Session, ship_id: int, updated_ship: models.Ship):
    ship = db.query(models.Ship).filter(models.Ship.ship_id == ship_id).first()
    if ship is None:
        return None
    for field, value in updated_ship.dict().items():
        setattr(ship, field, value)
    db.commit()
    db.refresh(ship)
    return ship


def delete_ship(db: Session, ship_id: int):
    ship = db.query(models.Ship).filter(models.Ship.ship_id == ship_id).first()
    if ship is None:
        return None
    db.delete(ship)
    db.commit()
    return ship


def create_port(db: Session, port: models.Port):
    db_port = models.Port(**port.dict())
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port


def get_ports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Port).offset(skip).limit(limit).all()


def get_port(db: Session, port_id: int):
    return db.query(models.Port).filter(models.Port.port_id == port_id).first()


def update_port(db: Session, port_id: int, updated_port: models.Port):
    port = db.query(models.Port).filter(models.Port.port_id == port_id).first()
    if port is None:
        return None
    for field, value in updated_port.dict().items():
        setattr(port, field, value)
    db.commit()
    db.refresh(port)
    return port


def delete_port(db: Session, port_id: int):
    port = db.query(models.Port).filter(models.Port.port_id == port_id).first()
    if port is None:
        return None
    db.delete(port)
    db.commit()
    return port


def create_container(db: Session, container: models.Container):
    db_container = models.Container(**container.dict())
    db.add(db_container)
    db.commit()
    db.refresh(db_container)
    return db_container


def get_containers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Container).offset(skip).limit(limit).all()


def get_container(db: Session, container_id: int):
    return db.query(models.Container).filter(models.Container.container_id == container_id).first()


def update_container(db: Session, container_id: int, updated_container: models.Container):
    container = db.query(models.Container).filter(models.Container.container_id == container_id).first()
    if container is None:
        return None
    for field, value in updated_container.dict().items():
        setattr(container, field, value)
    db.commit()
    db.refresh(container)
    return container


def delete_container(db: Session, container_id: int):
    container = db.query(models.Container).filter(models.Container.container_id == container_id).first()
    if container is None:
        return None
    db.delete(container)
    db.commit()
    return container


def create_item(db: Session, item: models.Item):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.item_id == item_id).first()


def update_item(db: Session, item_id: int, updated_item: models.Item):
    item = db.query(models.Item).filter(models.Item.item_id == item_id).first()
    if item is None:
        return None
    for field, value in updated_item.dict().items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.item_id == item_id).first()
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item
