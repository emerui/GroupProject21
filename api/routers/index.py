from . import orders
from . import order_details
from . import customers
from . import promotions
from . import order_options
from . import sandwiches


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(promotions.router)
    app.include_router(order_options.router)
    app.include_router(sandwiches.router)