from fastapi import FastAPI

app = FastAPI(title="Fast Api Advanced Challenges")
@app.get("/")
def read_root():
    return {"status": "healthy"}