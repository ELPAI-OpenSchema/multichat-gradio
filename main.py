from fastapi import FastAPI


app = FastAPI(root_path="/multichat")

@app.get("/")
async def root():
    return {"msg": "it works!"}

@app.get("/ping")
async def root():
    return {"msg": "pong!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)