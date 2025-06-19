from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.config import STOCK_PATH
from src.config import image_logo
from src.config import image_serge
order_dataframes = {}

def generate_order_summary(basket, user, total):
    """Format order summary for display."""
    summary = {
        "items": [
            f"- {item['name']} — ${item['price']} x {item.get('quantity', 1)}"
            for item in basket
        ],
        "total": f"${total}",
        "shipping_info": {
            "name": f"{user['first_name']} {user['last_name']}",
            "address": f"{user['street']}, {user['zip_code']} {user['city']}, {user['country']}",
            "contact": f"{user['email']} | {user['phone']}",
            "note": user.get("notes", "")
        }
    }
    return summary


def load_logo():
    return image_logo
def load_wine_inventory():
    return pd.read_csv(STOCK_PATH)

def load_serge():
    return image_serge
