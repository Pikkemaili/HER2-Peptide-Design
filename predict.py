import pandas as pd
from pathlib import Path

# 获取项目根目录
ROOT = Path(__file__).resolve().parent

# 1. 读取原始数据
candidates = pd.read_csv(ROOT / "data/candidates.csv")
af = pd.read_csv(ROOT / "results/alphafold_metrics.csv")
rmsd = pd.read_csv(ROOT / "results/rmsd_results.csv")
dock = pd.read_csv(ROOT / "results/docking_scores.csv")

# 2. 合并数据
df = candidates.merge(af, on="candidate_id", how="left")
df = df.merge(rmsd, on="candidate_id", how="left")
df = df.merge(dock[["candidate_id", "score"]], on="candidate_id", how="left")

# 3. 处理缺失值（未做对接的变体，分数为 NaN，统一替换为 "-"）
df["对接打分"] = df["score"].fillna("-")
df = df.drop(columns=["score"])

# 4. 按对接打分排序（负值越大越靠前），未对接的排在最后
df["_sort"] = df["对接打分"].apply(lambda x: float(x) if x != "-" else float('inf'))
df = df.sort_values(by="_sort", ascending=True).drop(columns=["_sort"])

# 5. 重命名列名以符合最终输出格式
df = df.rename(columns={
    "candidate_id": "候选编号",
    "sequence": "候选序列",
    "plddt": "pLDDT",
    "rmsd_vs_L": "RMSD_vs_L"
})

# 6. 输出最终结果
out_path = ROOT / "results"
out_path.mkdir(exist_ok=True)
df.to_excel(out_path / "results.xlsx", index=False)
print("已成功生成 results/results.xlsx")
print(df)
