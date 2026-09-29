import pandas as pd
from pathlib import Path

# 数据已更新：包含 HPEPDOCK 对接打分
data = [
    {"候选编号": "L",  "赛道": "赛道一", "候选序列": "LTVSPWY",
     "pLDDT": 82, "RMSD_vs_L": 0.000, "对接打分": -185.682,
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "原始线性肽",
     "结构文件": "results/alphafold_structures/L.cif"},
    {"候选编号": "L1", "赛道": "赛道一", "候选序列": "ATVSPWY",
     "pLDDT": 85, "RMSD_vs_L": 0.670, "对接打分": "-",
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "N端丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L1.cif"},
    {"候选编号": "L2", "赛道": "赛道一", "候选序列": "LAVSPWY",
     "pLDDT": 80, "RMSD_vs_L": 0.660, "对接打分": "-",
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "第2位丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L2.cif"},
    {"候选编号": "L3", "赛道": "赛道一", "候选序列": "LTASPWY",
     "pLDDT": 82, "RMSD_vs_L": 1.191, "对接打分": "-",
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "第3位丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L3.cif"},
    {"候选编号": "L4", "赛道": "赛道一", "候选序列": "LTVAPWY",
     "pLDDT": 80, "RMSD_vs_L": 1.956, "对接打分": "-",
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "第4位丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L4.cif"},
    {"候选编号": "L5", "赛道": "赛道一", "候选序列": "LTVSAWY",
     "pLDDT": 88, "RMSD_vs_L": 2.860, "对接打分": -198.400,
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "第5位丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L5.cif"},
    {"候选编号": "L6", "赛道": "赛道一", "候选序列": "LTVSPAY",
     "pLDDT": 94, "RMSD_vs_L": 5.655, "对接打分": "-",
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "第6位丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L6.cif"},
    {"候选编号": "L7", "赛道": "赛道一", "候选序列": "LTVSPWA",
     "pLDDT": 95, "RMSD_vs_L": 2.881, "对接打分": "-",
     "对应模型与运行版本": "AlphaFold 3 + HPEPDOCK 2.0",
     "备注": "第7位丙氨酸扫描变体",
     "结构文件": "results/alphafold_structures/L7.cif"},
]

df = pd.DataFrame(data)
out = Path("results")
out.mkdir(exist_ok=True)
df.to_excel(out / "results.xlsx", index=False)
print("已生成 results/results.xlsx")
print(df)
