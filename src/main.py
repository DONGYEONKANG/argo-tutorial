from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return f"안녕하세요. 저는 v0.0.10입니다. 😎"

if __name__ == "__main__":
    uvicorn.run(app="main:app", host='0.0.0.0', port=8080)
