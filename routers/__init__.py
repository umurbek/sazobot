from .start import router as start_router
from .search import router as search_router
from .callbacks import router as callbacks_router

routers = [start_router, search_router, callbacks_router]
