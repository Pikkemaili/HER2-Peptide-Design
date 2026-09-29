import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent

candidates = pd.read_csv(ROOT / "data/candidates.csv")
af = pd.read_csv(ROOT / "results/alphafold_metrics.csv")
rmsd = pd.read_csv(ROOT / "results/rmsd_results.csv")
dock = pd.read_csv(ROOT / "results/docking_scores.csv")

df = candidates.merge(af, on="candidate_id").merge(rmsd, on="candidate_id").merge(dock, on="candidate_id", how="left")
df["对接打分"] = df["score"].fillna("-")
df = df.sort_values(by="score", ascending=True)
df.to_excel(ROOT / "results/results.xlsx", index=False)
print("已生成 results/results.xlsx")
