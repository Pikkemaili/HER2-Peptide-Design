# AlphaFold Server 操作步骤

## 一、工具信息
- 名称：AlphaFold Server (AlphaFold 3)
- 网址：https://alphafoldserver.com
- 访问日期：2026-09-28

## 二、输入序列
L: LTVSPWY, L1: ATVSPWY, L2: LAVSPWY, L3: LTASPWY, 
L4: LTVAPWY, L5: LTVSAWY, L6: LTVSPAY, L7: LTVSPWA

## 三、操作步骤
1. 登录 alphafoldserver.com
2. 点击 "New job" -> "Add entity" -> 选择 "Protein"
3. 输入单条序列 (Copies=1，其余默认)
4. 提交并等待状态变为 "Completed"
5. 下载 .zip 压缩包，解压提取 `fold_XX_model_0.cif` 文件
6. 查看 `summary_confidences_0.json` 记录 ranking_score，查看 `full_data_0.json` 记录 pLDDT

## 四、结果说明
- 全局 ranking_score 均为 0.53，fraction_disordered=1.0（符合短肽高度柔性特征）。
- 局部 pLDDT 估算均值：L(≈82), L1(≈85), L2(≈80), L3(≈82), L4(≈80), L5(≈88), L6(≈94), L7(≈95)。
- 结构叠合 RMSD (vs L肽)：L1(0.670 Å), L2(0.660 Å), L3(1.191 Å), L4(1.956 Å), L5(2.860 Å), L6(5.655 Å), L7(2.881 Å)。
