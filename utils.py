import pandas as pd
from IPython.display import display, HTML
from typing import List
from vantage_sdk.core.http.models.shopping_assistant_group_result import (
    ShoppingAssistantGroupResult,
)


def display_row(df: pd.DataFrame, row_index: int) -> None:
    row = df.iloc[row_index]
    html_content = """
    <style>
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-family: Arial, sans-serif;
        }
        .data-table td {
            padding: 8px 15px;
            border: 1px solid #ddd;
            vertical-align: top;
        }
        .data-table .field-name {
            font-weight: bold;
            width: 25%;
        }
    </style>
    <table class='data-table'>
    """

    for field, value in row.items():
        html_content += f"""
        <tr>
            <td class='field-name'>{field}</td>
            <td>{value}</td>
        </tr>
        """

    html_content += "</table>"
    display(HTML(html_content))


def display_query_results(df: pd.DataFrame, results: List[str]) -> None:
    ids = [result.id for result in results]
    df_filtered = df[df["id"].isin(ids)].copy()
    df_filtered["id"] = pd.Categorical(df_filtered["id"], categories=ids, ordered=True)
    df_filtered = df_filtered.sort_values("id")

    html_content = """
    <style>
        .product-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start;
            gap: 15px;
        }
        .product-container {
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 8px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            width: 22%;
            box-sizing: border-box;
            overflow-y: auto;
            max-height: 400px;
        }
        .product-image {
            max-height: 250px;
            border-radius: 6px;
            margin-bottom: 10px;
            width: 100%;
            object-fit: contain;
        }
        .product-details {
            font-family: Arial, sans-serif;
            font-size: 12px;
            line-height: 1.4;
            color: #333;
            text-align: left;
        }
        .product-details strong {
            font-size: 14px;
            color: #0073e6;
        }
        @media (max-width: 768px) {
            .product-container {
                width: 48%;
            }
        }
        @media (max-width: 480px) {
            .product-container {
                width: 100%;
            }
        }
    </style>
    <h2>Search Results</h2>
    <div class='product-grid'>
    """
    for _, row in df_filtered.iterrows():
        html_content += f"""
        <div class='product-container'>
            <img src="{row['image_url']}" class='product-image'>
            <div class='product-details'>
                <strong>ID:</strong> {row['id']}<br>
                <strong>Title:</strong> {row['title']}<br>
                <strong>Color:</strong> {row['color']}<br>
                <strong>Brand:</strong> {row['brand']}<br>
                <strong>Gender:</strong> {row['gender']}<br>
                <strong>Product Type:</strong> {row['product_type']}<br>
                <strong>Style:</strong> {row['style']}<br>
                <strong>Price:</strong> {row['price']}<br>
                <strong>Price Range:</strong> {row['price_range']}<br>
                <strong>Availability:</strong> {row['availability']}<br>
                <strong>Description:</strong> {row['description']}<br>
            </div>
        </div>
        """

    html_content += "</div>"
    display(HTML(html_content))


def display_shopping_assistant_results(
    df: pd.DataFrame, groups: List[ShoppingAssistantGroupResult]
) -> None:
    html_content = """
    <style>
        .group-title {
            font-family: Arial, sans-serif;
            font-size: 20px;
            margin: 20px 0 10px;
            color: #0073e6;
        }
        .product-group {
            overflow-x: auto;
            white-space: nowrap;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .product-container {
            display: inline-block;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 8px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            width: 200px;
            max-height: 400px;
            margin-right: 15px;
            box-sizing: border-box;
            overflow-y: auto;
            overflow-x: hidden;
            word-wrap: break-word;
        }
        .product-image {
            max-height: 150px;
            border-radius: 6px;
            margin-bottom: 10px;
            width: 100%;
            object-fit: contain;
        }
        .product-details {
            font-family: Arial, sans-serif;
            font-size: 12px;
            line-height: 1.4;
            color: #333;
            text-align: left;
            white-space: normal;
        }
        .product-details strong {
            font-size: 14px;
            color: #0073e6;
        }
        @media (max-width: 768px) {
            .product-container {
                width: 48%;
            }
        }
        @media (max-width: 480px) {
            .product-container {
                width: 100%;
            }
        }
    </style>
    """

    for group in groups:
        html_content += f"<h2 class='group-title'>{group.group_name}</h2>"
        html_content += "<div class='product-group'>"

        ids = [result.id for result in group.results]
        df_filtered = df[df["id"].isin(ids)].copy()
        df_filtered["id"] = pd.Categorical(
            df_filtered["id"], categories=ids, ordered=True
        )
        df_filtered = df_filtered.sort_values("id")

        for _, row in df_filtered.iterrows():
            html_content += f"""
            <div class='product-container'>
                <img src="{row['image_url']}" class='product-image'>
                <div class='product-details'>
                    <strong>ID:</strong> {row['id']}<br>
                    <strong>Title:</strong> {row['title']}<br>
                    <strong>Color:</strong> {row['color']}<br>
                    <strong>Brand:</strong> {row['brand']}<br>
                    <strong>Gender:</strong> {row['gender']}<br>
                    <strong>Product Type:</strong> {row['product_type']}<br>
                    <strong>Style:</strong> {row['style']}<br>
                    <strong>Price:</strong> {row['price']}<br>
                    <strong>Price Range:</strong> {row['price_range']}<br>
                    <strong>Availability:</strong> {row['availability']}<br>
                    <strong>Description:</strong> {row['description']}<br>
                </div>
            </div>
            """
        html_content += "</div>"
    display(HTML(html_content))


def display_images(image_urls: List[str]) -> None:
    html_content = """
    <style>
        .product-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start;
            gap: 15px;
        }
        .product-container {
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 8px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            width: 22%;
            box-sizing: border-box;
            overflow-y: auto; /* Enable scrolling */
            max-height: 400px; /* Set maximum height for the product container */
        }
        .product-image {
            max-height: 250px; /* Larger image */
            border-radius: 6px;
            margin-bottom: 10px;
            width: 100%;
            object-fit: contain;
        }
        @media (max-width: 768px) {
            .product-container {
                width: 48%;
            }
        }
        @media (max-width: 480px) {
            .product-container {
                width: 100%;
            }
        }
    </style>
    <h2>Image Gallery</h2>
    <div class='product-grid'>
    """
    for image_url in image_urls:
        html_content += f"""
        <div class='product-container'>
            <img src="{image_url}" class='product-image'>
        </div>
        """
    html_content += "</div>"
    display(HTML(html_content))
