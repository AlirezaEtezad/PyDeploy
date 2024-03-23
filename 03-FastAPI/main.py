from fastapi import FastAPI, HTTPException,status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()



Sabzeh = {"farsi":"سبزه", "English": "Wheat",  "symbol": "Rebirth and growth", "image": "images/Sabzeh.jpg"}
Samanu = {"farsi":"سمنو", "English": "Samanu", "Symbol": "power and strength", "image": "images/Samanu.jpg"}
Senjed = {"farsi":"سنجد", "English": "Senjed", "symbol": "love and affection", "image": "images/Senjed.jpg"}
Seer =   {"farsi": "سیر", "English": "Garlic", "Symbol": "medicine and health", "image": "images/Seer.jpg"}
Seeb =   {"farsi": "سیب", "English": "Apple",  "symbol": "beauty and health.", "image": "images/Seeb.jpg"}
Somaq =  {"farsi":"سماق", "English": "Somaq",  "symbol": "sunrise and morale", "image": "images/Somagh.jpeg"}
Serkeh = {"farsi":"سرکه", "English": "Vinegar","symbol": "age and patience", "image": "images/Serkeh.jpg"}

haftsin = [Sabzeh,Samanu,Senjed,Seer,Seeb,Somaq,Serkeh]

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/")
def read_root():

    return "ُThis API will represent 7sin table; A sacred arrangement of 7 symbolic items. Each representing aspects of the natural world and spiritual values."

@app.get("/7sin")
def all():
    return haftsin 


@app.get("/7sin/{item}")
def get_item_info(item: str):
    for i in haftsin:
        if item == i["farsi"] or item == i["English"]:
            return i
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found in 7sin! choose between: Wheat,Samanu,Senjed,Garlic,Apple,Somaq,Vinegar")

@app.get("/7sin/{item}/image")
def show_image(item: str):
    for i in haftsin:
        if item == i["farsi"] or item == i["English"]:
            return FileResponse(f"{i['image']}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found in 7sin! choose between: Wheat,Samanu,Senjed,Garlic,Apple,Somaq,Vinegar")
    



# uvicorn main:app --reload --port 2000 --host 0.0.0.0