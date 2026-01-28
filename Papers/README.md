# 图像去雨文献库 (Image Deraining Literature)

> 整理关于单幅图像去雨 (Single Image Deraining) 的核心论文、复现笔记与实验结果。

---

## 🧭 分类索引 (Categorization)

| 类别 | 描述 | 路径 |
| :--- | :--- | :--- |
| **Traditional** | 基于物理先验与模型的方法 (GMM, Sparse Coding) | [浏览](./Traditional/) |
| **CNN-based** | 卷积神经网络经典模型 (DDN, PReNet) | [浏览](./CNN-based/) |
| **Transformer** | 基于注意力机制的高性能模型 (Restormer, Uformer) | [浏览](./Transformer-based/) |
| **Latest/SSM** | 2024-2026 前沿模型 (Mamba, Diffusion) | [浏览](./Mamba-based/) |

---

## 📝 近期阅读计划 (Reading Roadmap)

- [ ] **[2024]** Mamba-IR: A Generic Backbone for Image Restoration
- [ ] **[2022]** Restormer: Efficient Transformer for High-Resolution
- [x] **[2019]** PReNet: Progressive Image Deraining Networks

---

## 📊 统一指标对比 (Benchmark)
*注：以下数据均在 Rain100H 数据集上测得。*

| Model | PSNR (dB) | SSIM | Note |
| :--- | :--- | :--- | :--- |
| DDN | 27.33 | 0.827 | 开山之作 |
| PReNet | 29.46 | 0.899 | 强力 Baseline |
| **Your Repro** | -- | -- | 等待填入... |

[返回主页](../README.md)
