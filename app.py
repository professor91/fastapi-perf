"""
('1bbde323-0ed8-4c09-9c6d-e1bc66a90f63', '0alice0@example.com')
"""

from typing import Any, Tuple

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.datastructures import Headers

import sqlite3
import time

app = FastAPI()

conn: sqlite3.Connection = sqlite3.connect('db.sqlite')


@app.middleware('http')
async def auth_middleware(request: Request, call_next):
    print('in middleware')
    headers: Headers = request.headers
    if 'Authorization' not in headers.keys():
        pass
        # raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Token not Provided.')
    TOKEN: str = '1bbde323-0ed8-4c09-9c6d-e1bc66a90f63'
    cur: sqlite3.Cursor = conn.cursor()
    response: Any = cur.execute('SELECT * FROM token WHERE token = ?', (TOKEN,)).fetchone()
    if response == None:
        pass
        # raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Incorrect Token provided.')
    if not isinstance(response, tuple):
        pass
        # raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal Server Error.')
    print(response)
#
    response = await call_next(request)
    return response


@app.get("/")
async def root():
    print('in request')
    data: list[Tuple] = conn.cursor().execute('SELECT * from user;').fetchall()
    response = dict()
    for item in data:
        response[item[0]] = item[1]

    return {"data": response}

