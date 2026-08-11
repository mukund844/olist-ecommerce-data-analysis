import pandas as pd
import numpy as np

def build_master_table(tables):
    orders = tables["orders"].copy()
    items = tables["order_items"].copy()
    customers = tables["customers"].copy()
    products = tables["products"].copy()
    sellers = tables["sellers"].copy()

    orders["delivery_days"] = (
        orders["order_delivered_customer_date"]
        - orders["order_purchase_timestamp"]
    ).dt.days

    orders["estimated_days"] = (
        orders["order_estimated_delivery_date"]
        - orders["order_purchase_timestamp"]
    ).dt.days

    orders["delay_days"] = (
        orders["order_delivered_customer_date"]
        - orders["order_estimated_delivery_date"]
    ).dt.days

    orders["is_late"] = orders["delay_days"] > 0
    orders["order_year"] = orders["order_purchase_timestamp"].dt.year
    orders["order_month"] = orders["order_purchase_timestamp"].dt.month
    orders["order_month_name"] = orders["order_purchase_timestamp"].dt.month_name()
    orders["order_day_name"] = orders["order_purchase_timestamp"].dt.day_name()
    orders["order_hour"] = orders["order_purchase_timestamp"].dt.hour
    orders["order_year_month"] = orders["order_purchase_timestamp"].dt.to_period("M")

    master = (
        items
        .merge(orders, on="order_id", how="left")
        .merge(customers, on="customer_id", how="left")
        .merge(products, on="product_id", how="left")
        .merge(sellers, on="seller_id", how="left", suffixes=("", "_seller"))
    )

    master["item_revenue"] = master["price"] + master["freight_value"]
    master["same_state"] = master["customer_state"] == master["seller_state"]

    return master

def get_delivered(master):
    return master.loc[master["order_status"].eq("delivered")].copy()
