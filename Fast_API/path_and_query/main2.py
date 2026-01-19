#QUERY PARAMETER
from fastapi import FastAPI 

app = FastAPI() 
@app.get("/BOOKS")
async def books(limit: int):
        a = [
              {"1001" : "python"},
              {"1002" : "java"},
              {"1003" : "react"},
              {"1004" : "c++"},
              {"1005" : "javascript"}
        ]
        return {"book data is : {} ".format(a[:limit])}