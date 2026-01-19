from fastapi import FastAPI

app = FastAPI()

@app.get("/BOOKS/{Book_id},{Book_name}")
async def read_root(Book_id: int, Book_name: str):
    return {"Book_id": Book_id,
            "Book_name": Book_name
            }
