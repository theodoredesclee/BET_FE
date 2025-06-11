# Replaces the hardcoded path with a dynamic, relative one
from pathlib import Path
import os

BASE_DIR = "data"
project_root = Path(__file__).resolve().parents[1]

csv_path_ratings = project_root / 'data' / 'raw' / 'XWines_Slim_150K_ratings.csv'
csv_path_wines = project_root / 'data' / 'raw' / 'XWines_Full_100K_wines.csv'
image_logo = project_root / 'data' / 'image' / 'BET_logo.png'
BET_STOCK_PATH = project_root / "data" / "stock"
PROCESSED_DATA_PATH = project_root / "data" / "processed" / 'time_series.csv'
PROCESSED_DATA_PATH_WINE = project_root / "data" / "processed" / 'grapes_clustered.csv'
SHOPPING_LIST_PATH = project_root / "data" / "shopping_list"
PROCESSED_PATH = project_root / "data" / "processed"
STOCK = project_root / "data" / "stock"
STOCK_PATH = project_root / "data" / "stock" / "STOCK.csv"
SALE_HISTORY = project_root / "data" / "stock" / "Sale_history.csv"
MONTHLY_SALE = project_root / "data" / "stock" / "Monthly_sale.csv"
WINE_SHOPPING_LIST = project_root / "data" / "processed" / "wine_shopping_list.csv"

print("📁 project_root:", project_root)
print("📄 csv_path_wines:", csv_path_wines)
print("📄 csv_path_ratings:", csv_path_ratings)
