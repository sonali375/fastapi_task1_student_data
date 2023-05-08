from fastapi import FastAPI

app = FastAPI()


@app.get("/student")
async def root():
    return {"name": "Sonali Sahu"}, {"age": 22}, {"phone": 9437661099}, {"email": "sonalisahu2001@gmail.com"}
