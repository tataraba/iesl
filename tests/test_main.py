import pytest


@pytest.mark.asyncio
async def test_homepage_not_broken(client):
    """Make sure homepage is not broken."""
    response = await client.get("/")
    assert response.status_code == 200

