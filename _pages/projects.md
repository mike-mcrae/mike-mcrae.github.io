---
layout: archive
title: #"Projects"
permalink: /projects/
author_profile: true
---

## Southern Newswire Corpus - Historical Wire Articles (1960–1975)  
[View on GitHub](https://github.com/mikemcrae/southern-newswire) [arXiv article](https://arxiv.com) 🚀  
The **Southern Newswire Corpus** is a large-scale dataset of historical wire articles from U.S. Southern newspapers, spanning **1960–1975**. It covers multiple wire services (**AP**, **UPI**, and **NEA**) and offers both **raw OCR** and **LLM-corrected** versions. I developed a open-source pipeline tailored for the digitization of historical newspapers, which allows for performing multiple tasks.

**1. Parsing Layout:** The initial stage involves layout parsing, wherein articles, headlines, advertisements, and other content regions are identified from raw newspaper page scans. I introduce a newly trained layout detection model using Yolo v10. 

<p style="display: flex; justify-content: center;">
  <img src="/images/layout.jpg" alt="Race Dictionary Monthly" style="width: 30%;">
</p>

**2. Identification of newswire service:** I develop three fine-tuned BERT models to identify whether aricles are written by the Associated Press (AP), United Press International (UPI), or Newspaper Enterprise Association (NEA). 

<p style="display: flex; justify-content: space-between;">
  <img src="/images/2.ap_upi_nea_proportions.svg" alt="Event Study Q1-Q4" style="width: 40%;">
 <img src="/images/3.topics_over_time.svg" alt="Race Dictionary Monthly" style="width: 40%;">
</p>

**3. Duplication identification:** I adopt a noise-robust de-duplication approach (Silcock et al., 2024) to identify replications of the same underlying dispatch, allowing for comparison between local versions of non-local news.  

<p style="display: flex; justify-content: space-between;">
  <img src="/images/news1b.png" alt="Event Study Q1-Q4" style="width: 40%;">
 <img src="/images/news2b.png" alt="Race Dictionary Monthly" style="width: 48%;">
</p>

**4. LLM-Based Text Correction:** I developed a text-correction pipeline that uses Llama3.2, a large language model configured for minimal rewriting. Llama\,3.2 corrects common OCR artefacts such as misread characters, broken words, or stray punctuation, improving text clarity without introducing anachronistic spellings, while preserving paragraph structure and historical language. Corrections are limited to unambiguous OCR errors, ensuring that archaic or dialect terms remain intact.


### Results:
- **Neural Networks**: Used a fine-tuned BERT model to identify wire services.
- **Machine Learning for OCR Correction**: Leveraged Llama 3.2 to correct noisy OCR outputs.
- **Article Clustering**: Employed Sentence-BERT embeddings to detect shared wire dispatches.
- **Topic Modeling**: Used LDA and BERTopic to identify news themes.

**Final Dataset:** 9.57 million wire articles detected from 58 million total articles.  

---

## 🛠️ Project 2 - Coming Soon  
Placeholder for a future project on **Neural Networks**, **Machine Learning OCR**, or other exciting work! Stay tuned for updates. 😊

Would you like me to help you style this for your Jekyll theme? 🚀
