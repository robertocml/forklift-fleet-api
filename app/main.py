from fastapi import FastAPI

app = FastAPI(
    title="Forklift Fleet API",
    version="0.1.0",
    description="API FOR FORKLIFT FLEET."
)

@app.get("/root")
def root():
    return {"status": "ok", "message": "initial endpoint"}