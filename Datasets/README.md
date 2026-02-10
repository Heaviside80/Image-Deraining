# 🌧️ Image Deraining Dataset Collection

本仓库用于系统性地收集和整理单幅图像去雨（Single Image Deraining）领域的基准数据集。涵盖了从经典合成雨条（Synthetic Streaks）到最新的真实世界双焦昼夜雨滴（Real-world Dual-focused）等多种退化场景。

## 📌 收集状态概览 (Collection Status)

- [x] 基础合成数据集 (Rain100H/L, Rain14000)
- [x] 真实世界对齐数据集 (GT-RAIN)
- [x] 2025前沿数据集 (Raindrop Clarity)
- [x] 统一预处理脚本编写

---

## 📂 数据集清单 (Dataset List)

### 1. 真实世界数据集 (Real-World Paired)
*核心目标：解决 Sim2Real 域鸿沟，提升模型泛化能力。*

| 数据集名称 | 发布年份/会议 | 核心特点 | 状态 | 官方链接 |
| :--- | :--- | :--- | :--- | :--- |
| **GT-RAIN** | 2022 ECCV | 包含真实雨痕与雨雾（Rain Accumulation），全球多场景 | ⏳ 待处理 | [Link](https://github.com/UCLA-VMG/GT-RAIN) |
| **Raindrop Clarity** | 2025 NTIRE | **双焦（Dual-focused）**，昼夜场景，复杂光照 | 📥 下载中 | [Link](https://cvlai.net/ntire/2025/) |
| **SPA-Data** | 2019 CVPR | 真实视频序列提取，侧重小雨纹理 | ✅ 已入库 | [Link](https://github.com/stevewongv/SPA-Data) |

### 2. 合成数据集 (Synthetic Benchmarks)
*核心目标：架构验证与消融实验。*

| 数据集名称 | 来源 | 特点 | 规模 (Train/Test) | 状态  | 官方链接 |
| :--- | :------  | :--- | :--- | :--- |:--- |
| **Rain100H** | CVPR 2017 | 5种方向重度雨条，极其经典 | 1800 / 100 |✅ 已入库|
| **Rain100L** | CVPR 2017 | 轻度雨条，侧重细节恢复 | 200 / 100 | ✅ 已入库 |
| **Rain14000** | CVPR 2017 | 大规模合成数据，适合模型预训练 | 14000 / 1000 | ✅ 已入库|



---

## 🛠️ 数据预处理 (Data Preparation)

为了统一模型输入，所有收集到的数据集建议遵循以下目录结构：

```text
/data
  ├── GT-RAIN
  │   ├── train_input  # 有雨图像 (Rainy)
  │   └── train_target # 清晰图像 (Ground Truth)
  ├── Rain100H
  │   ├── train
  │   └── test
  └── ...

