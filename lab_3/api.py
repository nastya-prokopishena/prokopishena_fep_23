from typing import List

from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session

import crud
import database
import schemas

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/ship/", response_model=schemas.Ship)
def create_ship(ship: schemas.Ship, db: Session = Depends(get_db)):
    return crud.create_ship(db, ship)


@app.get("/ship/", response_model=List[schemas.Ship])
def get_ships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_ships(db, skip, limit)


@app.get("/ship/{ship_id}", response_model=schemas.Ship)
def get_ship(ship_id: int, db: Session = Depends(get_db)):
    return crud.get_ship(db, ship_id)


@app.put("/ship/{ship_id}", response_model=schemas.Ship)
def update_ship(ship_id: int, updated_ship: schemas.Ship, db: Session = Depends(get_db)):
    return crud.update_ship(db, ship_id, updated_ship)


@app.delete("/ship/{ship_id}")
def delete_ship(ship_id: int, db: Session = Depends(get_db)):
    return crud.delete_ship(db, ship_id)


@app.post("/port/", response_model=schemas.Port)
def create_port(port: schemas.Port, db: Session = Depends(get_db)):
    return crud.create_port(db, port)


@app.get("/port/", response_model=List[schemas.Port])
def get_ports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_ports(db, skip, limit)


@app.get("/port/{port_id}", response_model=schemas.Port)
def get_port(port_id: int, db: Session = Depends(get_db)):
    return crud.get_port(db, port_id)


@app.put("/port/{port_id}", response_model=schemas.Port)
def update_port(port_id: int, updated_port: schemas.Port, db: Session = Depends(get_db)):
    return crud.update_port(db, port_id, updated_port)


@app.delete("/port/{port_id}")
def delete_port(port_id: int, db: Session = Depends(get_db)):
    return crud.delete_port(db, port_id)


@app.post("/containers/", response_model=schemas.Container)
def create_container(container: schemas.Container, db: Session = Depends(get_db)):
    return crud.create_container(db, container)


@app.get("/containers/", response_model=List[schemas.Container])
def get_containers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_containers(db, skip, limit)


@app.get("/containers/{container_id}", response_model=schemas.Container)
def get_container(container_id: int, db: Session = Depends(get_db)):
    return crud.get_container(db, container_id)


@app.put("/containers/{container_id}", response_model=schemas.Container)
def update_container(container_id: int, updated_container: schemas.Container, db: Session = Depends(get_db)):
    return crud.update_container(db, container_id, updated_container)


@app.delete("/containers/{container_id}")
def delete_container(container_id: int, db: Session = Depends(get_db)):
    return crud.delete_container(db, container_id)


@app.post("/item/", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@app.get("/item/", response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)


@app.get("/item/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_item(db, item_id)


@app.put("/item/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, updated_item: schemas.Item, db: Session = Depends(get_db)):
    return crud.update_item(db, item_id, updated_item)


@app.delete("/item/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id)
