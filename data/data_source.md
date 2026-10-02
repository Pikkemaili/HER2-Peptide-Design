# 数据来源说明

## 多肽序列
- L肽 (LTVSPWY)：来源于公开文献报道。
- L1-L7 丙氨酸扫描变体：本项目基于L肽序列自行设计。
- 获取方式：公开文献，无使用限制。

## 受体结构 6BGT
- 来源：RCSB PDB (https://www.rcsb.org/structure/6BGT)
- 描述：Trastuzumab Fab mutant in complex with HER2 extracellular domain
- 分辨率：2.7 Å
- 获取日期：2026-09-10
- 许可：PDB公共数据，可自由使用。

### 6BGT 结构处理说明
- 使用 HPEPDOCK 在线平台默认的预处理流程。
- 下载的 6BGT.pdb 未经手动去水或去配体处理。
- 多肽配体作为对接时的构象采样对象，最终以对接打分排序为准。

## 在线平台
- AlphaFold2 (Colab网页端)：https://colab.research.google.com/
- HPEPDOCK 2.0：http://huanglab.phys.hust.edu.cn/hpepdock/

## 本地分析工具
- PyMOL：用于多肽结构可视化、结构叠合与 RMSD 计算，详细说明见 `models/PyMOL_usage.md`。
