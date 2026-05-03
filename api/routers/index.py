from . import orders, order_details, customers, promotions, order_options, sandwiches


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(promotions.router)
    app.include_router(order_options.router)
    app.include_router(sandwiches.router)
