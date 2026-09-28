import pandas as pd
from pathlib import Path

# 填入候选序列。HPEPDOCK跑完后，在"关键预测指标"里填入对接打分
data = [
    {"候选编号": "L",  "赛道": "赛道一", "候选序列": "LTVSPWY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "线性肽", "结构文件": "results/alphafold_structures/L.pdb"},
    {"候选编号": "L1", "赛道": "赛道一", "候选序列": "ATVSPWY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L1.pdb"},
    {"候选编号": "L2", "赛道": "赛道一", "候选序列": "LAVSPWY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L2.pdb"},
    {"候选编号": "L3", "赛道": "赛道一", "候选序列": "LTASPWY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L3.pdb"},
    {"候选编号": "L4", "赛道": "赛道一", "候选序列": "LTVAPWY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L4.pdb"},
    {"候选编号": "L5", "赛道": "赛道一", "候选序列": "LTVSAWY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L5.pdb"},
    {"候选编号": "L6", "赛道": "赛道一", "候选序列": "LTVSPAY", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L6.pdb"},
    {"候选编号": "L7", "赛道": "赛道一", "候选序列": "LTVSPWA", "关键预测指标": "", "对应模型与运行版本": "AlphaFold Server + HPEPDOCK 2.0", "备注": "丙氨酸扫描变体", "结构文件": "results/alphafold_structures/L7.pdb"},
]

df = pd.DataFrame(data)
out = Path("results")
out.mkdir(exist_ok=True)
df.to_excel(out / "results.xlsx", index=False)
print("已生成 results/results.xlsx")
