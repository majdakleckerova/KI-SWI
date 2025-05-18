import pandas as pd

def prumer_znamek(df: pd.DataFrame) -> pd.Series:
    df["znamka"] = pd.to_numeric(df["znamka"], errors="coerce")
    prumerne_znamky = df.groupby("predmet")["znamka"].mean()
    
    return prumerne_znamky