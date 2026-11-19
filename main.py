import math
import os
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/fib")
async def fib(n: int = Query(..., ge=0, le=40)):
    return {"n": n, "result": fibonacci(n)}


@app.get("/gcd")
async def gcd(
    a: int = Query(..., ge=1, le=1_000_000),
    b: int = Query(..., ge=1, le=1_000_000),
):
    return {"a": a, "b": b, "result": math.gcd(a, b)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
