# Swin UNETR — Vision Transformers for 3D Brain Tumor Segmentation

**Medical Computer Vision · 3D Semantic Segmentation · Swin Transformers · Multi-modal MRI**

This project is based on the Swin UNETR research paper. Implementation details and project-specific evaluation results will be documented as development progresses.

## Overview

A project exploring **Swin UNETR** for the semantic segmentation of brain tumors in **3D MRI volumes**.

The reference architecture combines a **hierarchical Swin Transformer encoder** with a **convolutional decoder**. It uses multi-scale representations and skip connections to produce voxel-level tumor-region predictions.

## Objective

Study and work toward implementing a transformer-based approach to brain tumor segmentation, following the methodology described by Hatamizadeh et al.

## Reference Architecture

The following describes the architecture in the paper, rather than a completed implementation in this repository.

- **3D patch embedding:** converts volumetric MRI inputs into tokens.
- **Hierarchical Swin Transformer encoder:** extracts features at multiple resolutions.
- **Shifted-window self-attention:** enables interactions across window boundaries while controlling attention cost.
- **Convolutional decoder:** reconstructs spatial segmentation maps.
- **Multi-scale skip connections:** connect encoder features to the decoder.
- **Soft Dice loss:** the training objective used in the reference study.

## MRI Inputs & Segmentation Targets

The reference study uses the **BraTS 2021** dataset with four MRI input channels:

| MRI modality | Description |
| --- | --- |
| T1 | Native T1-weighted MRI |
| T1c / T1Gd | Contrast-enhanced T1-weighted MRI |
| T2 | T2-weighted MRI |
| FLAIR | Fluid-attenuated inversion recovery MRI |

The segmentation outputs represent three overlapping tumor regions:

| Target | Region |
| --- | --- |
| WT | Whole tumor |
| TC | Tumor core |
| ET | Enhancing tumor |

Dataset selection, access, and preprocessing for this project are not yet documented.

## Reference Implementation & Evaluation

The paper's implementation uses **PyTorch** and **MONAI**. Its evaluation includes **Dice scores** and **Hausdorff distances** for the tumor regions.

These provide a reference for future development. This project's framework configuration, training settings, hardware, and evaluation protocol remain to be documented.

## Current Status

- **Research basis:** Swin UNETR paper identified as the project reference.
- **Implementation:** in progress; completed components have not yet been specified.
- **Training and evaluation:** no project-specific results reported yet.

The paper's benchmark scores are not results achieved by this project.

## Reference

Ali Hatamizadeh, Vishwesh Nath, Yucheng Tang, Dong Yang, Holger R. Roth, and Daguang Xu. **Swin UNETR: Swin Transformers for Semantic Segmentation of Brain Tumors in MRI Images.** BrainLes 2021, published in 2022, pp. 272–284.

- [Paper DOI](https://doi.org/10.1007/978-3-031-08999-2_22)
- [Reference implementation](https://monai.io/research/swin-unetr)
