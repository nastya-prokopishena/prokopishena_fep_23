from fastapi import FastAPI, HTTPException
from shemas.Customer import Customer, OrderFacade

app = FastAPI()
order_facade = OrderFacade()


def register_and_process_order(order_data_path: str):
    try:
        customer = Customer("1")
        order_facade.register_customer(customer)
        order_facade.process_order(order_data_path)
        return {"message": "Order processing complete"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@app.post("/process_order/{order_data_path}")
def process_order(order_data_path: str):
    return register_and_process_order(order_data_path)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
