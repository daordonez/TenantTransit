from fastapi import FastAPI

# Create an instance of the FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to TenantTransit!"}