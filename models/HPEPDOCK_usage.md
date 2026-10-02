# HPEPDOCK 2.0 使用说明与工具卡

## 工具信息
- 名称：HPEPDOCK 2.0
- 类型：多肽-蛋白分子对接计算工具（非AI模型）
- 网址：http://huanglab.phys.hust.edu.cn/hpepdock/
- 来源：华中科技大学黄胜友教授课题组
- 访问日期：2026-09-10
- 使用许可：仅用于非商业学术研究

## 输入输出
- 输入：受体结构 `data/6BGT.pdb` 和多肽序列（FASTA格式）。
- 输出：对接打分（Docking Score）、对接后的复合物PDB结构文件。

## 调用参数
- Receptor：6BGT.pdb
- Peptide：LTVSPWY (L肽) 和 LTVSAWY (L5肽)
- 其他参数：默认

## 已知局限
- 对接打分是计算预测结果，不能完全等同于真实结合亲和力，需实验验证。
- 短肽高度柔性，对接结果可能存在一定不确定性。
