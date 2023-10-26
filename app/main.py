import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    item: str


@app.get("/data", response_model=Data)
async def get_data() -> Data:
    """
    Get Data
    """
    undefined_variable

    return Data(item="devops")


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
