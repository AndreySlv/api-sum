from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/health")
def health():
    return {"status": "ok"}