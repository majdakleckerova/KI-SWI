import pandas as pd

def trzby_za_zakazniky(df: pd.DataFrame) -> pd.Series:
    # filtr 2024
    df["datum"] = pd.to_datetime(df["datum"])
    df_2024 = df[df["datum"].dt.year == 2024]
    
    # trzba == mnozstvi * cena
    df_2024["trzba"] = df_2024["mnozstvi"] * df_2024["cena"]
    
    # agregace podle zakaznika
    trzby = df_2024.groupby("zakaznik")["trzba"].sum()
    
    return trzby