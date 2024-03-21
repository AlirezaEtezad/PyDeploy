from fastapi import FastAPI, HTTPException,status

app = FastAPI()



Sabzeh = {"farsi":"سبزه", "English": "Wheat",  "symbol": "Rebirth and growth"}
Samanu = {"farsi":"سمنو", "English": "Samanu", "Symbol": "power and strength"}
Senjed = {"farsi":"سنجد", "English": "Senjed", "symbol": "love and affection"}
Seer =   {"farsi": "سیر", "English": "Garlic", "Symbol": "medicine and health"}
Seeb =   {"farsi": "سیب", "English": "Apple",  "symbol": "beauty and health."}
Somaq =  {"farsi":"سماق", "English": "Somaq",  "symbol": "sunrise and morale"}
Serkeh = {"farsi":"سرکه", "English": "Vinegar","symbol": "age and patience"}

haftsin = [Sabzeh,Samanu,Senjed,Seer,Seeb,Somaq,Serkeh]


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


# uvicorn fast_API:app --reload --port 2000 --host 0.0.0.0
    