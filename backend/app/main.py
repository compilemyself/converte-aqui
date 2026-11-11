
from fastapi import FastAPI

app = FastAPI(
    title="ConverteAqui API",
    description=(
        "API REST do ConverteAqui, uma aplicação web para conversão, "
        "compressão e redimensionamento de imagens."
    ),
    version="0.1.0",
)


@app.get("/", tags=["Informações"])
async def read_root() -> dict[str, str]:
    "Retorna informações básicas sobre a API."
    return {
        "name": "ConverteAqui API",
        "version": app.version,
        "documentation": "/docs",
    }


@app.get("/api/v1/health", tags=["Monitoramento"])
async def health_check() -> dict[str, str]:
    """Confirma que o serviço ConverteAqui está respondendo.

    A conexão com o PostgreSQL ainda precisa ser feita. [WIP]
    """
    return {
        "status": "ok",
        "service": "converteaqui-api",
    }