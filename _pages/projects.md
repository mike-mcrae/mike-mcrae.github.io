---
title: Projects
layout: default
---

# 📊 Southern Newswires Dataset

## 🗞️ Overview
This page documents the Southern Newswires dataset, which identifies articles from wire services such as **AP**, **UPI**, and **NEA** in Southern newspapers.

## 📂 Dataset Details
- **Source:** Southern newspaper archives (1960–1973)  
- **Articles:** 58 million articles from 250 newspapers  
- **Labels:** AP, UPI, NEA (binary classifications)  
- **Format:** JSON  

## 🧵 Data Structure
The dataset consists of JSON files with the following keys:

```json
{
  "article_id": "12345",
  "newspaper": "Atlanta Daily",
  "date": "1965-03-15",
  "headline": "Civil Rights March",
  "AP": 1,
  "UPI": 0,
  "NEA": 0
}
```

## 🚀 How the Dataset Was Built
- **Model:** Fine-tuned BERT on Southern newspaper articles  
- **Training Data:** Manually labeled samples from 1960-1973  
- **Classes:** AP, UPI, NEA  

## 📈 Results
- **Precision:** 94%  
- **Recall:** 91%  
- **F1 Score:** 92%  

---

### 📥 Download
The dataset is available [here](https://huggingface.co/username/southern-newswires).

### 📝 Citation
If you use this dataset, please cite:

```
@dataset{yourname_2025,
  author    = {Your Name},
  title     = {Southern Newswires Dataset},
  year      = {2025},
  publisher = {GitHub},
  url       = {https://github.com/username/repository}
}
```

---
**Back to:** [Home](index.md)
