import pandas as pd

def build_rfm(delivered_df):
    base = (
        delivered_df
        .groupby(["customer_unique_id", "order_id"])
        .agg(
            order_value=("item_revenue", "sum"),
            order_date=("order_purchase_timestamp", "first"),
        )
        .reset_index()
    )

    snapshot_date = base["order_date"].max() + pd.Timedelta(days=1)

    rfm = base.groupby("customer_unique_id").agg(
        recency=("order_date", lambda d: (snapshot_date - d.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("order_value", "sum"),
    )

    rfm["R_score"] = pd.qcut(
        rfm["recency"], q=4, labels=[4, 3, 2, 1]
    ).astype(int)

    rfm["F_score"] = pd.qcut(
        rfm["frequency"].rank(method="first"),
        q=4, labels=[1, 2, 3, 4]
    ).astype(int)

    rfm["M_score"] = pd.qcut(
        rfm["monetary"], q=4, labels=[1, 2, 3, 4]
    ).astype(int)

    rfm["RFM_total"] = rfm[["R_score", "F_score", "M_score"]].sum(axis=1)

    def label_segment(score):
        if score >= 10:
            return "Champions"
        if score >= 8:
            return "Loyal"
        if score >= 6:
            return "Potential"
        if score >= 4:
            return "At Risk"
        return "Lost"

    rfm["segment"] = rfm["RFM_total"].apply(label_segment)
    return rfm
