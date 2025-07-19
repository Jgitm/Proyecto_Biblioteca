import time
from fastapi import Request

async def logger_middleware(request: Request, call_next):
    inicio = time.time()
    response = await call_next(request)
    duracion = round(time.time() - inicio, 3)
    print(f"🛰 {request.method} {request.url.path} → {duracion}s")
    return response