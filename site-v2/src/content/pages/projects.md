---
title: "Projects"
permalink: /projects/
author_profile: true
---

## Southern Newswires - Extracting Historical Wire Articles
Replication, Data, & Models - [GitHub Repository](https://github.com/mike-mcrae/southern-newswires). 
Preliminary Article - [arXiv](http://arxiv.org/abs/2502.11866) 

I developed a open-source pipeline tailored for the digitisation of historical newspapers, which allows for performing multiple tasks. This pipeline can be used to generate large-scale datasets of historical wire articles from U.S. newspapers. In practise, it was used to extract wire articles from Southern Newspapers over the period 1960 - 1975 to prepare the dataset for a forthcoming paper by the author. This dataset covers multiple wire services (**AP**, **UPI**, and **NEA**) and offers both **raw OCR** and **LLM-corrected** versions. I developed a open-source pipeline tailored for the digitization of historical newspapers, which allows for performing multiple tasks. 

**1. Parsing Layout:** Articles, headlines, advertisements, and other content regions are identified from raw newspaper page scans. A newly trained layout detection model using Yolo v10 is introduced and available soon at [GitHub](https://github.com/mike-mcrae/southern-newswires). Articles which span multiple bounding boxes are combined with a rule-based association which uses bounding-box coordinates to merge them into a single structured observation, preserving the headline, author byline (where identifiable), and article text. 


**2. Identification of newswire service:** I develop three fine-tuned BERT models to identify whether aricles are written by the Associated Press (AP), United Press International (UPI), or Newspaper Enterprise Association (NEA) ([Models](https://huggingface.co/mikemcrae25/newswire_classifiers)).

<div style="display: flex; justify-content: center; gap: 40px;">
  <img src="/images/2.ap_upi_nea_proportions.svg" alt="Event Study Q1-Q4" style="width: 40%;">
  <img src="/images/3.topics_over_time.svg" alt="Race Dictionary Monthly" style="width: 40%;">
</div>

**3. Duplication identification:** I adopt a noise-robust de-duplication approach (Silcock et al., 2024) to identify replications of the same underlying dispatch, allowing for comparison between local versions of non-local news.  

**4. LLM-Based Text Correction:** I developed a text-correction pipeline that uses Llama3.2, a large language model configured for minimal rewriting. Llama3.2 corrects common OCR artefacts such as misread characters, broken words, or stray punctuation, improving text clarity without introducing anachronistic spellings, while preserving paragraph structure and historical language. Corrections are limited to unambiguous OCR errors, ensuring that archaic or dialect terms remain intact.

**Final Dataset:** 9.57 million wire articles from 58 million total articles.  
**Observations:** article_id, underlying_wire_id, newspaper_title, date, location, headline, author, newswire_service, raw_article, corrected_article, topic.

---
