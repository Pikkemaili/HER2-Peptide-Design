# HER2靶向多肽的计算设计与筛选

## 一、项目说明
本项目属于赛道一：AI大分子与多肽药物设计。
基于文献报道的 HER2 靶向多肽 LTVSPWY，利用 AlphaFold2 (Colab网页端) 预测其及 7 个丙氨酸扫描变体（L1-L7）的三维结构，
并结合 PyMOL 计算 RMSD 分析突变引起的构象变化。随后利用 HPEPDOCK 2.0 将筛选出的代表肽段与 HER2 胞外域（PDB: 6BGT）进行分子对接，
筛选出结合力更强的候选多肽，并计划通过后续湿实验对关键位点进行验证，为 HER2 靶向降解药物设计提供依据。

## 二、使用工具
- AlphaFold2 (Colab网页端)，访问日期：2026-09-09
- HPEPDOCK 2.0，在线版，访问日期：2026-09-10
- PyMOL (版本 3.1.8)，用于结构叠合与 RMSD 计算

## 三、候选筛选与排序规则
1. 首先通过 AlphaFold2 预测 8 条候选肽（L及L1-L7）的三维结构，计算 pLDDT 局部置信度。
2. 使用 PyMOL 将 L1-L7 与原始 L 肽进行结构叠合，计算 RMSD，评估突变引起的构象变化程度。结果显示 L1-L4 的 RMSD 极小（<0.6 Å），而 L5 的 RMSD 显著升高至 2.305 Å，表明第 5 位突变导致了显著的构象重排。
3. 结合 RMSD 分析结果（L5构象变化显著），选取原始肽 L 和候选肽 L5 进入 HPEPDOCK 分子对接复筛。**其余候选（L1-L4, L6-L7）未进行对接，在结果表中记为“-”，不参与最终打分排序。**
4. 最终排序以 HPEPDOCK 对接打分（负值越大结合越强）为准：L5（-198.400）优于原始肽 L（-185.682）。
5. **后续实验计划**：基于以上计算与对接结果，已选定 L5（第5位突变）作为最优候选，后续将通过湿实验（如定点突变、结合亲和力测定等）对第2、5位点进行进一步验证。

## 四、运行环境
本项目核心计算使用在线平台，无需本地GPU。
运行 `predict.py` 需要：Python 3.10+，pandas，openpyxl
依赖见 `requirements.txt`。

## 五、运行命令
```bash
pip install -r requirements.txt
python predict.py

## 六、对接复合物可视化
本项目使用 PyMOL 3.1.8 对 HPEPDOCK 对接的复合物进行结合模式分析。可视化脚本保存在 `src/` 目录下：
- `src/visualize_L.pml`：查看原始肽 L 与 HER2 的结合模式。
- `src/visualize_L5.pml`：查看 L5 变体与 HER2 的结合模式。

使用方法：
1. 启动 PyMOL，在命令行输入 `cd 到仓库根目录`。
2. 输入 `@src/visualize_L.pml` 或 `@src/visualize_L5.pml`。
3. 脚本会自动加载 6BGT 和对接复合物，显示结合口袋、氢键和关键残基标签。

生成的结合口袋图已保存在 `results/docking_visualization/`。
