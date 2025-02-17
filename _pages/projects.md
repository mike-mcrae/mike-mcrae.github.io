---
layout: archive
title: #"Projects"
permalink: /projects/
author_profile: true
---

## Southern Newswire Corpus - Historical Wire Articles (1960–1975)
Replication, Data, & Models - [GitHub Repository](https://github.com/mikemcrae/southern-newswire). 
Preliminary Article - [arXiv](https://arxiv.com) 

The **Southern Newswire Corpus** is a large-scale dataset of historical wire articles from U.S. Southern newspapers, spanning **1960–1975**. It covers multiple wire services (**AP**, **UPI**, and **NEA**) and offers both **raw OCR** and **LLM-corrected** versions. I developed a open-source pipeline tailored for the digitization of historical newspapers, which allows for performing multiple tasks.  

**1. Parsing Layout:** Articles, headlines, advertisements, and other content regions are identified from raw newspaper page scans. A newly trained layout detection model using Yolo v10 is introduced and available soon at [GitHub](https://github.com/mikemcrae/southern-newswire). 

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
  <img src="/images/news1b.png" alt="news1" style="width: 40%;">
 <img src="/images/news2b.png" alt="news2" style="width: 40%;">
</p>

**4. LLM-Based Text Correction:** I developed a text-correction pipeline that uses Llama3.2, a large language model configured for minimal rewriting. Llama3.2 corrects common OCR artefacts such as misread characters, broken words, or stray punctuation, improving text clarity without introducing anachronistic spellings, while preserving paragraph structure and historical language. Corrections are limited to unambiguous OCR errors, ensuring that archaic or dialect terms remain intact.

**Final Dataset:** 9.57 million wire articles detected from 58 million total articles.  
**Observations:** article_id, underlying_wire_id, newspaper_title, date, location, headline, author, newswire_service, raw_article, corrected_article, topic.
---


## 🛠️ The American Newspaper Corpus (1960–1975) - Coming Soon  
A **nationwide historical newspaper corpus** covering **all U.S. newspapers** from **1960–1975**. This dataset will provide a **comprehensive view** of how newspapers across different regions covered major events, political shifts, and cultural changes.

### Key Features:
- **Full newspaper archives**, not just newswire articles.
- **Advanced OCR correction** using fine-tuned language models.
- **Topic and sentiment analysis** to track media discourse over time.
- **Comparisons across states and political leanings** to analyze media bias and framing.

🚀 Stay tuned for updates as this dataset develops! 
