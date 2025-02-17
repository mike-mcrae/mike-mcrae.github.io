---
title: Southern Newswire Corpus
layout: default
---

# 📊 Southern Newswire Corpus: A Large-Scale Dataset of Mid-Century Wire Articles Beyond the Front Page

## 🗞️ Overview
The **Southern Newswire Corpus** is a large-scale dataset of historical wire articles from U.S. Southern newspapers, spanning **1960–1975**. It covers multiple wire services, including **Associated Press (AP)**, **United Press International (UPI)**, and **Newspaper Enterprise Association (NEA)**. Unlike prior work focusing solely on front-page content, this dataset captures articles across entire newspapers, offering broader insights into mid-century Southern coverage.

This dataset also includes a **cleaned version** processed through an **LLM-based text correction pipeline** to reduce OCR noise, enhancing suitability for **quantitative text analysis**. Additionally, duplicate versions of articles are retained to enable **editorial variation analysis**, allowing researchers to study how local newspapers modified syndicated content.

## 📂 Dataset Details
- **Source:** Digitized Southern newspapers (1960–1975)  
- **Articles:** 57.5 million total articles, 9.57 million newswire articles  
- **Wire Services:** AP, UPI, NEA  
- **Unique Wire Articles:** 1.76 million  
- **Versions:** Raw OCR and LLM-corrected text  
- **Format:** JSON

## 🧵 Data Structure
Each article follows the format:

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

## 📊 Dataset Statistics
The following table summarizes the corpus contents:

| Metric | Count |
|--------|-------|
| Total Articles | 57,547,723 |
| Newswire Articles | 9,571,254 |
| AP Articles | 7,429,704 |
| UPI Articles | 2,024,254 |
| NEA Articles | 117,296 |
| Unique Newswire Articles | 1,768,567 |
| Unique AP Articles | 1,326,036 |
| Unique UPI Articles | 393,015 |
| Unique NEA Articles | 49,516 |

## 📈 Visualizing the Dataset
### 📰 Article Density Over Time
![Density of all articles by date](south_pages_histogram.pdf)

### 📉 Evolution of Newswires (1960–1975)
#### Newswire vs. All Articles Over Time
![Newswire vs. All Articles](1.nw_vs_all_articles.pdf)

#### AP, UPI, and NEA Proportions Over Time
![Wire Service Proportions](2.ap_upi_nea_proportions.pdf)

#### Evolution of Proportional Newswires
![Proportional Newswires](1b.nw_vs_all_articles_prop.pdf)

#### County-Level Circulation Coverage
![Circulation Coverage](circulation.png)

## 🔍 Methodology
### 🗂️ Layout Analysis and OCR
- YOLOv10-based layout detection to identify articles, headlines, and advertisements.
- **OCR:** Tesseract OCR for text extraction, followed by **LLM-based correction** using **Llama 3.2** to reduce errors.

### 🏷️ Newswire Classification
- Three **BERT-based classifiers** trained on labeled historical newspaper articles.
- **Precision:** AP (99.25%), UPI (99.99%), NEA (98.76%).
- **Training Details:** TPU v2-8, batch size 64, learning rate 2 × 10⁻⁵.

### 🔗 Identifying Shared Wire Dispatches
- Articles with high semantic similarity are **grouped by a shared article ID**.
- **No deduplication**—local variations are preserved for editorial comparison.

## 📥 Download
The dataset is available [here](https://huggingface.co/username/southern-newswires).

## 📝 Citation
```
@dataset{mcrae_2025,
  author    = {Michael McRae},
  title     = {Southern Newswire Corpus},
  year      = {2025},
  publisher = {GitHub},
  url       = {https://github.com/mikemcrae/southern-newswire}
}
```

## 🔮 Future Directions
- Expanding dataset coverage to **all U.S. states** (1960–1975).
- Enhancing **OCR correction** using open-source models.
- Improving **topic modeling** via transformer embeddings.

---

🔙 **Back to:** [Home](index.md)
