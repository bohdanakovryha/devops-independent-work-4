from molotov import scenario

URL = "http://localhost:8000/api/health"


@scenario(weight=100)
async def health_returns_json(session):
    async with session.get(URL) as resp:
        assert resp.status == 200
        assert resp.headers["Content-Type"].startswith("application/json")
        data = await resp.json()
        assert data["status"] == "ok"
