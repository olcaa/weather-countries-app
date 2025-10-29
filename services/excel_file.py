import pandas as pd
from config import Config
import os

def append_to_excel(row: dict):
    path = Config.EXCEL_FILEPATH

    df_new = pd.DataFrame([row])
    if os.path.exists(path):
        try:
            df_old = pd.read_excel(path)
            df_updated = pd.concat([df_old, df_new], ignore_index=True)
        except:
            df_updated = df_new
    else:
        df_updated = df_new

    df_updated.to_excel(path, index=False)