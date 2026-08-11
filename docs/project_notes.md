# Project Notes

## Source

This repository was organised from the supplied Olist end-to-end analysis notebook.

## Data grain

The reusable pipeline builds the master dataset at order-item level, then derives
order/customer/seller/category analyses from that table.

## Important modelling choice

Customer retention is measured with `customer_unique_id`, not `customer_id`, because
the same real customer can appear under multiple order-specific customer IDs.

## Reproducibility

Keep the raw CSV filenames unchanged. The notebook and pipeline use those canonical names.
