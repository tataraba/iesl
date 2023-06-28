from contextlib import asynccontextmanager

import pytest
import pytest_asyncio
from app.main import app
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient


@pytest_asyncio.fixture
async def async_app():
    @asynccontextmanager
    async def lifespan(_app):
        print("Starting up")
        yield
        print("Shutting down")

    async with LifespanManager(app) as manager:
        print("Inside lifespan")
        yield manager.app


@pytest_asyncio.fixture
async def client(async_app):
    async with AsyncClient(app=async_app, base_url="http://test") as _client:
        yield _client
