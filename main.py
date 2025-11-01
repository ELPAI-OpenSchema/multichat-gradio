from fastapi import FastAPI


# Serve the app on both root paths and the /multichat prefix so an ingress
# that forwards the /multichat path (without stripping) will still work.
app = FastAPI(root_path="/multichat")

# Also expose the same endpoints under the /multichat prefix. This is the
# simplest fix when the ingress controller does not strip the prefix.
@app.get("/")
async def multichat_root():
    return {"msg": "it works!"}


@app.get("/ping")
async def multichat_ping():
    return {"msg": "pong!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)