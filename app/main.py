"""FastAPI-приложение для работы с платежами."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.payments import (
    providers_router,
    router as payments_router,
    tariffs_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan контекст приложения."""
    yield


app = FastAPI(
    title="Payment API",
    description="API для создания платежей по тарифам подписки",
    lifespan=lifespan,
)

app.include_router(payments_router)
app.include_router(tariffs_router)
app.include_router(providers_router)
