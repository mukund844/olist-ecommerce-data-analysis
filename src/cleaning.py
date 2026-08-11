import pandas as pd

ORDER_DATE_COLS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

def clean_tables(tables):
    orders = tables["orders"].copy()
    items = tables["order_items"].copy()
    payments = tables["payments"].copy()
    reviews = tables["reviews"].copy()
    customers = tables["customers"].copy()
    products = tables["products"].copy()
    sellers = tables["sellers"].copy()
    geo = tables["geolocation"].copy()
    category = tables["category_translation"].copy()

    # Exact duplicate handling: the original analysis identifies geolocation
    # as the table requiring duplicate removal.
    geo = geo.drop_duplicates().reset_index(drop=True)

    for col in ORDER_DATE_COLS:
        if col in orders.columns:
            orders[col] = pd.to_datetime(orders[col], errors="coerce")

    customers["customer_city"] = customers["customer_city"].str.strip().str.lower()
    sellers["seller_city"] = sellers["seller_city"].str.strip().str.lower()

    products = products.merge(
        category, on="product_category_name", how="left"
    )

    if "product_category_name_english" in products.columns:
        products = products.rename(
            columns={"product_category_name_english": "category"}
        )

    return {
        "orders": orders,
        "order_items": items,
        "payments": payments,
        "reviews": reviews,
        "customers": customers,
        "products": products,
        "sellers": sellers,
        "geolocation": geo,
        "category_translation": category,
    }
