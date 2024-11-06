from fastapi import FastAPI

app = FastAPI()

@app.get("/ete")
def read_root():
    return {"Hello": "World"}