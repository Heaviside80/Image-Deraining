### 1. 基本信息 (Basic Info)

* **论文标题**: SwinIR: Image Restoration Using Swin Transformer
* **发表渠道/年份**: ICCV 2021 (图像复原领域的经典必读)
* **核心关键词**: Swin Transformer, Image Restoration, Super-resolution, Denoising
* **资源链接**: [Paper](https://arxiv.org/abs/2108.10257) | [Code](https://github.com/JingyunLiang/SwinIR)

---

### 2. 核心贡献 (Key Contributions)

> *一句话总结：本文提出了一种基于 Swin Transformer 的通用图像复原基准模型，解决了 CNN 在处理长程依赖关系上的局限性。*

* **Point 1**: 证明了 Transformer 在低层视觉任务（SR, Denoising, JPEG压缩去除）上可以全面超越 CNN。
* **Point 2**: 引入了**浅层特征提取、深层特征提取和图像重建**三阶段架构。
* **Point 3**: 采用了基于窗口的自注意力机制，大大降低了计算复杂度。

---

### 3. 技术路径 (Methodology)

#### 3.1 退化模型 (Degradation Model)

针对超分辨率任务：


*其中  为原图， 为模糊核， 为下采样， 为加性噪声。*

#### 3.2 网络架构 (Architecture)

* **Shallow Feature Extraction**: 使用一个  的卷积层提取初步特征。
* **Deep Feature Extraction (RSTB)**: 核心模块是 **Residual Swin Transformer Blocks (RSTB)**。每个 RSTB 包含多个 Swin Transformer 层和一个残差连接卷积层。
* **HQ Image Reconstruction**: 通过像素洗牌（Pixel Shuffle）或卷积层恢复图像细节。

#### 3.3 核心模块：Swin Transformer Layer (STL)

* **W-MSA**: 在局部窗口内计算注意力，减少计算量。
* **SW-MSA**: 通过“移位窗口”解决窗口间的信息隔离问题，实现全局建模。

---

### 4. 实验结果 (Experiments)

#### 4.1 核心指标对比 (以经典超分 Set5 数据集为例)

| Method | Scale | PSNR ↑ | SSIM ↑ | Params |
| --- | --- | --- | --- | --- |
| **SwinIR (Ours)** |  | **38.42** | **0.9623** | 11.8M |
| RCAN (CNN-based) |  | 38.27 | 0.9614 | 15.6M |

#### 4.2 视觉效果

*SwinIR 在恢复重复纹理（如建筑栅栏、百叶窗）时，比 CNN 产生的伪影更少，线条更锐利。*

---

### 5. 个人心得与启发 (Insights)

* **值得借鉴的点**: 残差连接在 Transformer 架构中依然至关重要；SwinIR 展示了**局部注意力+移位窗口**在恢复细节上的强大能力。
* **局限性**: 虽然计算量比全注意力小，但在高分辨率（如 4K）实时处理上依然面临压力。
* **后续实验建议**: 尝试在自己的去雾模型中，将主干从 ResNet 替换为 RSTB 模块，观察 PSNR 是否有实质性提升。

---

### 💡 GitHub 操作小贴士：

你可以把上面的内容保存为 `notes/SwinIR_2021.md`。如果你在读论文时发现作者开源了模型权重，记得在 **Basic Info** 里加上权重下载链接，这样下次你要做对比实验时，直接看 GitHub 笔记就能找到资源。

**下一步你想让我帮你找一篇 2024-2025 年最新的图像复原论文（例如基于 Diffusion 的）来做类似的总结吗？**
