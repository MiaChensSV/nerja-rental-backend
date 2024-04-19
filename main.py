from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI(
    title="nerja-rental-backend",
    description="This is a collection of APIs for nerja rental application",
    version="0.1.0",
    docs_url="/swagger",
    redoc_url=None
)

@app.get("/", response_class=RedirectResponse)
def read_root():
    """
    Redirects '/' to '/swagger'
    """
    return "/swagger"

