# AI-900 Azure AI Fundamentals Prep Plan

Purpose: This is a one-stop, end-to-end study plan to help you prepare for and pass Microsoft Azure AI Fundamentals (AI-900). It combines official links, study sequencing, domain notes, practice strategy, glossary, and exam-style questions in one place.

**Location and usage note:** This file lives at the repo root (`AI-900_PREP_PLAN.md`). Use it as your daily checklist: study the domain sections, run the knowledge checks, complete sample questions, then validate with Microsoft practice assessments.

## Table of Contents
- [Quick links](#quick-links)
- [Recommended plan (fast + thorough)](#recommended-plan-fast--thorough)
  - [7-day sprint plan](#7-day-sprint-plan)
  - [14-day plan](#14-day-plan)
- [Exam logistics](#exam-logistics)
- [Skills at a glance study sections](#skills-at-a-glance-study-sections)
  - [AI workloads + Responsible AI](#ai-workloads--responsible-ai)
  - [Machine learning fundamentals](#machine-learning-fundamentals)
  - [Computer vision workloads + Azure services](#computer-vision-workloads--azure-services)
  - [NLP workloads + Azure services](#nlp-workloads--azure-services)
  - [Generative AI workloads + Azure services](#generative-ai-workloads--azure-services)
- [Glossary (AI-900)](#glossary-ai-900)
- [Sample questions (with answers)](#sample-questions-with-answers)
- [Practice strategy](#practice-strategy)
- [Resources](#resources)

## Quick links
- Official certification page (Microsoft Learn):  
  https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
- Official study guide (skills measured):  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900
- Practice assessments:  
  https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications
- Register and schedule exam:  
  https://learn.microsoft.com/en-us/credentials/certifications/register-schedule-exam
- Pearson VUE Microsoft landing page (optional):  
  https://www.pearsonvue.com/us/en/microsoft.html

## Recommended plan (fast + thorough)

### 7-day sprint plan
- **Day 1:** Read [Exam logistics](#exam-logistics), then study [AI workloads + Responsible AI](#ai-workloads--responsible-ai), do that section's knowledge check.
- **Day 2:** Study [Machine learning fundamentals](#machine-learning-fundamentals), run knowledge check, review key metric terms in [Glossary (AI-900)](#glossary-ai-900).
- **Day 3:** Study [Computer vision workloads + Azure services](#computer-vision-workloads--azure-services), do questions tagged CV in [Sample questions](#sample-questions-with-answers).
- **Day 4:** Study [NLP workloads + Azure services](#nlp-workloads--azure-services), do questions tagged NLP.
- **Day 5:** Study [Generative AI workloads + Azure services](#generative-ai-workloads--azure-services), do questions tagged GenAI.
- **Day 6:** Do full [Sample questions](#sample-questions-with-answers) timed, patch weak areas via glossary and domain sections.
- **Day 7:** Execute [Practice strategy](#practice-strategy) final loop and [Final 24-hour review plan](#final-24-hour-review-plan).

### 14-day plan
- **Week 1 (build understanding):**
  - Day 1-2: [AI workloads + Responsible AI](#ai-workloads--responsible-ai) + glossary responsible AI terms.
  - Day 3-4: [Machine learning fundamentals](#machine-learning-fundamentals) + confusion matrix and metrics.
  - Day 5: [Computer vision workloads + Azure services](#computer-vision-workloads--azure-services).
  - Day 6: [NLP workloads + Azure services](#nlp-workloads--azure-services).
  - Day 7: Light review + first 20 [Sample questions](#sample-questions-with-answers).
- **Week 2 (exam execution):**
  - Day 8: [Generative AI workloads + Azure services](#generative-ai-workloads--azure-services).
  - Day 9-10: Full [Sample questions](#sample-questions-with-answers), focus mistakes by domain.
  - Day 11: Microsoft practice assessment pass 1 (timed).
  - Day 12: Microsoft practice assessment pass 2 (closed notes), drill weak objectives.
  - Day 13: [Readiness checklist](#readiness-checklist) and 30-second explanations.
  - Day 14: [Final 24-hour review plan](#final-24-hour-review-plan), rest, exam.

## Exam logistics
- **Duration:** Microsoft certification page lists **45 minutes for this assessment**.
- **Price:** Microsoft states: **"Price based on the country or region in which the exam is proctored."**  
  Practical note: many candidates see pricing around **$99 USD**, but final cost varies by region, tax, and discounts.
- **Where to sign up:** Use **Schedule exam** from the certification page. Delivery partners include Pearson VUE and Certiport (availability varies by location).
- **Passing score:** **700/1000** (per study guide).
- **Exam language/accommodations:** Confirm current options on the certification and scheduling pages before booking.

## Skills at a glance study sections

## AI workloads + Responsible AI

### What you must be able to do
- Identify common AI workloads and map them to business scenarios.
- Explain responsible AI principles and practical implications.
- Distinguish between prediction, perception, language, and generative use cases.

### Key concepts
- AI workloads: machine learning, computer vision, NLP, conversational AI, generative AI.
- Responsible AI principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability.
- Human-in-the-loop and governance basics.

### Azure services to know
- Azure AI Foundry (portal and model workflow context).
- Azure AI services (vision, language, speech, decision-oriented features where relevant).
- Azure OpenAI Service.
- Azure AI Content Safety.

### Common pitfalls / trick questions
- Treating responsible AI as only a legal topic. It is design + testing + operations.
- Confusing transparency with exposing model weights. Often it means explainability and disclosure.
- Assuming "accurate" automatically means "fair." These are different quality dimensions.

### Mini knowledge check (6)
1. Which principle is most directly tied to documenting model limits?  
2. You need to ensure users know they are interacting with AI. Which principle is this closest to?  
3. Is it possible for a high-accuracy model to still violate fairness goals?  
4. What is a human-in-the-loop control used for?  
5. Which is a better responsible AI action: one-time review at launch, or continuous monitoring?  
6. Name two AI workloads that can be combined in one app.

---

## Machine learning fundamentals

### What you must be able to do
- Differentiate regression, classification, and clustering.
- Identify features vs labels and train/validation/test roles.
- Interpret confusion matrix and precision/recall tradeoffs.
- Explain overfitting and basic mitigation.

### Key concepts
- Supervised vs unsupervised learning.
- Feature engineering and label quality.
- Split strategy: train, validation, test.
- Metrics: accuracy, precision, recall, F1, MAE, RMSE.
- Overfitting vs underfitting.

### Azure services to know
- Azure Machine Learning (high-level role in model lifecycle).
- Azure AutoML (conceptual fit for low-code training).
- ML endpoints/deployment concepts.

### Common pitfalls / trick questions
- Using accuracy only on imbalanced classes.
- Mixing up false positive and false negative impacts.
- Thinking test data is used for tuning.
- Confusing clustering with classification.

### Mini knowledge check (7)
1. Is predicting house price classification or regression?  
2. Is spam/not-spam classification or clustering?  
3. In a confusion matrix, what does precision optimize against?  
4. What does recall optimize against?  
5. Why keep a test set untouched until final evaluation?  
6. Give one sign of overfitting.  
7. For medical screening, which is usually prioritized first: precision or recall?

---

## Computer vision workloads + Azure services

### What you must be able to do
- Distinguish image classification, object detection, OCR, and face-related capabilities.
- Match scenarios to Azure vision services.
- Understand what image captioning and spatial extraction can and cannot do.

### Key concepts
- Image classification: one or more labels for whole image.
- Object detection: class + bounding box location.
- OCR/read: extract text from images/documents.
- Image analysis: tags, captions, dense descriptions (service-dependent).

### Azure services to know
- Azure AI Vision.
- Azure AI Document Intelligence (forms, structured extraction).
- Face-related capabilities in Azure AI Vision/Face APIs (depending on region/policy constraints).

### Common pitfalls / trick questions
- Confusing object detection with image classification.
- Assuming OCR returns business fields automatically without schema/extraction logic.
- Ignoring model/data quality issues such as blurry images and domain drift.

### Mini knowledge check (6)
1. "Find every car and where it is in the image." Classification or detection?  
2. "Extract invoice number and date from scanned invoice." Which service family fits best?  
3. What does OCR return at minimum?  
4. Can classification tell you where an object is located?  
5. Which task is closer to "read text from street sign image"?  
6. Name one risk that harms vision accuracy in production.

---

## NLP workloads + Azure services

### What you must be able to do
- Explain tokenization, stop words, stemming, lemmatization at a practical level.
- Distinguish key phrase extraction, sentiment analysis, entity recognition, and translation.
- Choose suitable language services for QnA/chat and text analytics.

### Key concepts
- Tokenization and normalization.
- Entity extraction and PII handling basics.
- Sentiment polarity and confidence.
- Language detection and translation.
- Embeddings for semantic similarity/search.

### Azure services to know
- Azure AI Language (sentiment, key phrase, entity, conversational language capabilities).
- Azure AI Translator.
- Azure AI Speech (speech-to-text/text-to-speech context for language workloads).

### Common pitfalls / trick questions
- Assuming stemming and lemmatization are interchangeable outputs.
- Treating sentiment as objective truth rather than model inference.
- Confusing keyword extraction with full semantic understanding.

### Mini knowledge check (6)
1. Which process turns raw text into tokens?  
2. Which is more linguistically correct: stemming or lemmatization?  
3. Which service family supports sentiment and entity extraction?  
4. Is translation the same as summarization?  
5. What are embeddings primarily used for in modern NLP pipelines?  
6. Why can sarcasm hurt sentiment model quality?

---

## Generative AI workloads + Azure services

### What you must be able to do
- Explain prompts, tokens, grounding, and retrieval-augmented generation (RAG).
- Identify safe usage patterns for generative AI systems.
- Differentiate base model, fine-tuning, and prompt engineering at a high level.

### Key concepts
- Prompt structure and instructions.
- Tokens and context window constraints.
- Grounding with enterprise data (RAG).
- Hallucination risk and mitigation.
- Safety filters, policy checks, and red teaming basics.

### Azure services to know
- Azure OpenAI Service.
- Azure AI Search (for retrieval + grounding in RAG designs).
- Azure AI Content Safety.
- Azure AI Foundry (orchestration and evaluation workflows).

### Common pitfalls / trick questions
- Assuming model output is always factual.
- Confusing RAG with model fine-tuning.
- Ignoring token limits and cost implications.
- Deploying without abuse/safety controls.

### Mini knowledge check (7)
1. What is a token in LLM systems?  
2. Why use RAG instead of only prompting a base model?  
3. Does RAG change model weights?  
4. Name one way to reduce hallucinations.  
5. Which service helps enforce content safety checks?  
6. What is grounding in one sentence?  
7. Why track prompt/output evaluation over time?

---

## Glossary (AI-900)

1. **Accuracy** - Ratio of correct predictions to total predictions.  
   **AI-900 context:** Useful baseline metric, but weak on imbalanced datasets.

2. **Accountability** - Responsibility for AI outcomes, controls, and governance.  
   **AI-900 context:** One of Microsoft Responsible AI principles.

3. **Anomaly detection** - Identifying rare patterns that differ from normal behavior.
4. **API** - Programmatic interface used to call cloud AI services.
5. **AutoML** - Automated model selection and tuning workflow.
6. **Azure AI Foundry** - Azure environment for building and evaluating AI solutions.
7. **Azure AI Language** - Service family for text analytics and language tasks.
8. **Azure AI Search** - Search and retrieval service used often in RAG.
9. **Azure AI Vision** - Service family for image analysis and vision tasks.
10. **Azure OpenAI Service** - Azure-hosted access to OpenAI models with enterprise controls.
11. **Bag of Words** - Text representation using term counts by vocabulary.
12. **Bias (model bias)** - Systematic skew producing unfair outcomes across groups.
13. **Classification** - Predicting discrete categories, such as spam/not spam.
14. **Clustering** - Grouping unlabeled data by similarity.
15. **Confusion matrix** - Table of TP, TN, FP, FN for classification outcomes.
16. **Content Safety** - Policy and filtering controls for harmful AI inputs/outputs.
17. **Context window** - Maximum token span the model can consider at once.
18. **Corpus** - Collection of text documents used for analysis/training.
19. **Data drift** - Input data distribution shifts over time, reducing model reliability.
20. **Embeddings** - Dense numeric vectors encoding semantic meaning of text/images.  
   **AI-900 context:** Core to semantic search and RAG retrieval.
21. **Entity (NER)** - Named real-world object in text, like person or location.
22. **Evaluation set** - Held-out data used to assess model behavior.
23. **Explainability** - Ability to understand why a model made a prediction.
24. **Fairness** - AI outcomes should avoid unjustified disparate impact.
25. **False negative (FN)** - Positive instance predicted as negative.
26. **False positive (FP)** - Negative instance predicted as positive.
27. **Feature** - Input variable used by a model.
28. **Fine-tuning** - Additional training on a base model for specific behavior.
29. **F1 score** - Harmonic mean of precision and recall.
30. **Generative AI** - Models that create new content such as text or images.
31. **Grounding** - Constraining model responses with trusted external context.
32. **Hallucination** - Fluent but incorrect model output.
33. **Human-in-the-loop** - Human review/approval integrated into AI workflow.
34. **Inclusiveness** - Designing AI to serve diverse users and abilities.
35. **Inference** - Producing predictions from a trained model.
36. **Intent** - User goal inferred from language input.
37. **Key phrase extraction** - Identifying important terms in a document.
38. **Label** - Target value to predict in supervised learning.
39. **Lemmatization** - Reducing words to dictionary base form (lemma).
40. **Machine learning** - Models that learn patterns from data.
41. **MAE** - Mean absolute error for regression.
42. **Model endpoint** - Deployed API endpoint serving model predictions.
43. **NLP** - Natural language processing for machine understanding of text/speech.
44. **Object detection** - Identifying objects and their locations in images.
45. **OCR** - Optical character recognition for text extraction from images.
46. **Overfitting** - Model memorizes training data and generalizes poorly.
47. **PII** - Personally identifiable information requiring protection.
48. **Precision** - Of predicted positives, proportion that are truly positive.
49. **Prompt** - Instruction/context given to a generative model.
50. **RAG** - Retrieval-augmented generation combining retrieval with LLM output.
51. **Recall** - Of actual positives, proportion correctly identified.
52. **Regression** - Predicting continuous numeric values.
53. **Reliability and safety** - AI should perform consistently and avoid harm.
54. **Responsible AI** - Practical framework for safe, fair, trustworthy AI.
55. **RMSE** - Root mean squared error for regression.
56. **Sentiment analysis** - Estimating emotional polarity in text.
57. **Stop words** - Very common words often removed in preprocessing.
58. **Stemming** - Heuristic suffix stripping to reduce word variants.
59. **Supervised learning** - Learning from labeled examples.
60. **Temperature** - Decoding parameter controlling output randomness in LLMs.
61. **Token** - Basic text unit consumed/produced by language models.
62. **Tokenization** - Splitting text into tokens.
63. **Topic modeling** - Discovering latent themes in document collections.
64. **Train/validation/test split** - Data partitioning for fit, tuning, and final check.
65. **Transparency** - Communicating AI system behavior and limitations.
66. **True negative (TN)** - Negative instance correctly predicted negative.
67. **True positive (TP)** - Positive instance correctly predicted positive.
68. **Underfitting** - Model too simple to capture useful patterns.
69. **Unsupervised learning** - Learning from unlabeled data.
70. **Word sense disambiguation** - Selecting the correct meaning of a word by context.

## Sample questions (with answers)

> Format mix: multiple choice (MCQ), select all that apply (SATA), matching, and scenario-based.  
> Tags: `[AI] [ML] [CV] [NLP] [GenAI] [RAI]`.

### Q1 [AI][RAI] MCQ
Which Responsible AI principle most directly relates to documenting model limitations?
- A. Inclusiveness
- B. Transparency
- C. Reliability and safety
- D. Accountability  
**Answer:** B  
**Why:** Transparency includes communicating system capabilities, limits, and assumptions.

### Q2 [ML] MCQ
Predicting a house price is:
- A. Classification
- B. Clustering
- C. Regression
- D. Anomaly detection  
**Answer:** C  
**Why:** Price is continuous numeric output.

### Q3 [ML] SATA
Which statements are true about precision and recall?
- A. Precision penalizes false positives.
- B. Recall penalizes false negatives.
- C. Recall is always higher than precision.
- D. Both are derived from confusion matrix terms.  
**Answer:** A, B, D  
**Why:** C is not generally true.

### Q4 [CV] MCQ
You need class labels plus bounding boxes for objects in images. Choose:
- A. OCR
- B. Image classification
- C. Object detection
- D. Translation  
**Answer:** C  
**Why:** Detection returns class + location.

### Q5 [NLP] MCQ
Reducing "studies" to "study" is typically:
- A. Tokenization
- B. Stemming
- C. Lemmatization
- D. Translation  
**Answer:** C  
**Why:** Lemmatization targets dictionary base forms.

### Q6 [GenAI] MCQ
RAG primarily helps by:
- A. Increasing model size
- B. Changing model weights
- C. Grounding responses with retrieved context
- D. Removing token limits  
**Answer:** C  
**Why:** Retrieval adds relevant external context.

### Q7 [AI][RAI] MCQ
An accurate model still shows worse outcomes for one demographic group. This is mainly a:
- A. Scalability issue
- B. Fairness issue
- C. Availability issue
- D. Cost issue  
**Answer:** B  
**Why:** Fairness addresses differential impact across groups.

### Q8 [ML] MCQ
Which dataset split should remain untouched until final evaluation?
- A. Training set
- B. Validation set
- C. Test set
- D. Inference set  
**Answer:** C  
**Why:** Test set is for final unbiased estimate.

### Q9 [NLP] Matching
Match each term to best description:
1. Tokenization
2. Stop words
3. Embeddings
4. Sentiment analysis

a. Dense vectors for semantic meaning  
b. Breaking text into units  
c. Common low-information words  
d. Polarity estimation

**Answer:** 1-b, 2-c, 3-a, 4-d  
**Why:** Standard NLP mapping.

### Q10 [CV] MCQ
Extracting text from a scanned receipt is:
- A. Object detection
- B. OCR
- C. Clustering
- D. Speech recognition  
**Answer:** B  
**Why:** OCR is designed for text extraction from images.

### Q11 [GenAI] SATA
Which are practical hallucination mitigations?
- A. Ground with trusted retrieval
- B. Add output verification/validation
- C. Increase temperature
- D. Constrain system prompts  
**Answer:** A, B, D  
**Why:** Higher temperature often increases variation risk.

### Q12 [ML] MCQ
High training accuracy but low test accuracy indicates:
- A. Underfitting
- B. Overfitting
- C. Data encryption
- D. Normalization  
**Answer:** B  
**Why:** Model memorized training data patterns.

### Q13 [AI] MCQ
Which is an AI workload?
- A. Object storage replication
- B. Natural language processing
- C. DNS resolution
- D. Subnet routing  
**Answer:** B  
**Why:** NLP is a core AI workload.

### Q14 [NLP] Scenario
You need language detection, key phrase extraction, and sentiment in one pipeline. Best fit:
- A. Azure AI Vision
- B. Azure AI Language
- C. Azure AI Search only
- D. Azure Machine Learning only  
**Answer:** B  
**Why:** Language service covers these text analytics tasks.

### Q15 [RAI] MCQ
Which principle best aligns with keeping a clear owner for model incidents?
- A. Transparency
- B. Accountability
- C. Inclusiveness
- D. Privacy  
**Answer:** B  
**Why:** Accountability defines ownership and responsibility.

### Q16 [ML] MCQ
Spam vs non-spam is:
- A. Regression
- B. Clustering
- C. Binary classification
- D. Dimensionality reduction  
**Answer:** C  
**Why:** Two discrete classes.

### Q17 [CV] MCQ
Whole-image label "cat" without location uses:
- A. Object detection
- B. Image classification
- C. OCR
- D. Segmentation  
**Answer:** B  
**Why:** Classification labels the entire image.

### Q18 [GenAI] MCQ
Token budget mainly affects:
- A. Image resolution
- B. Prompt + response length constraints
- C. Data encryption
- D. Region availability only  
**Answer:** B  
**Why:** Context window is token-based.

### Q19 [NLP] SATA
Which are true about stemming?
- A. Output is always a valid dictionary word
- B. It reduces word variants
- C. It can improve consistency
- D. It is usually heuristic  
**Answer:** B, C, D  
**Why:** A is false for stemming.

### Q20 [ML] Scenario
A fraud model misses many actual fraud cases. Primary metric to improve:
- A. Precision
- B. Recall
- C. MAE
- D. R-squared  
**Answer:** B  
**Why:** Missed positives are false negatives, recall issue.

### Q21 [RAI] MCQ
Collecting only one accent for speech data most directly harms:
- A. Transparency
- B. Inclusiveness
- C. Accountability
- D. Tokenization  
**Answer:** B  
**Why:** Underrepresentation harms inclusiveness and fairness.

### Q22 [CV] Scenario
Need to read key-value fields from forms at scale:
- A. Azure AI Vision tags
- B. Azure AI Document Intelligence
- C. Azure AI Translator
- D. Azure OpenAI only  
**Answer:** B  
**Why:** Designed for structured document extraction.

### Q23 [GenAI] MCQ
Which statement is correct?
- A. RAG updates model weights during every query.
- B. RAG retrieves context and injects it into prompt flow.
- C. RAG removes need for source documents.
- D. RAG is only for images.  
**Answer:** B  
**Why:** Retrieval enriches prompts without retraining.

### Q24 [ML] MCQ
Which metric is for regression?
- A. Precision
- B. Recall
- C. RMSE
- D. F1  
**Answer:** C  
**Why:** RMSE is regression error metric.

### Q25 [NLP] MCQ
Embeddings are best described as:
- A. Rule-based keyword lists
- B. Dense vectors encoding semantics
- C. Raw token IDs only
- D. OCR output  
**Answer:** B  
**Why:** Embeddings encode meaning in vector space.

### Q26 [AI][RAI] SATA
Good Responsible AI operations include:
- A. Monitor model drift
- B. Keep incident response owner
- C. Skip retraining forever
- D. Track outcome parity metrics  
**Answer:** A, B, D  
**Why:** Continuous monitoring is required.

### Q27 [CV] MCQ
Which task likely needs bounding polygons and layout understanding?
- A. Topic modeling
- B. Document OCR/layout extraction
- C. Regression
- D. Clustering  
**Answer:** B  
**Why:** Document extraction uses layout + text.

### Q28 [NLP] MCQ
Word sense disambiguation solves:
- A. Sentence splitting
- B. Choosing correct meaning of ambiguous words
- C. Language translation
- D. OCR errors  
**Answer:** B  
**Why:** Context determines intended sense.

### Q29 [GenAI] Scenario
A chatbot cites nonexistent policy sections. Best immediate fix:
- A. Increase temperature
- B. Add retrieval grounding to approved policy docs
- C. Remove content filters
- D. Reduce prompt length to 1 sentence  
**Answer:** B  
**Why:** Grounding reduces unsupported claims.

### Q30 [ML] Matching
Match term to definition:
1. FP
2. FN
3. TP
4. TN

a. Positive predicted positive correctly  
b. Negative predicted positive incorrectly  
c. Positive predicted negative incorrectly  
d. Negative predicted negative correctly

**Answer:** 1-b, 2-c, 3-a, 4-d  
**Why:** Standard confusion matrix definitions.

### Q31 [NLP] MCQ
Key phrase extraction primarily provides:
- A. Full logical proof of document
- B. Important terms/phrases
- C. Bounding boxes
- D. Numeric regression score  
**Answer:** B  
**Why:** It surfaces salient phrases.

### Q32 [GenAI] SATA
Prompt engineering usually involves:
- A. Clear role/instructions
- B. Output format constraints
- C. Retrieval context when needed
- D. Forced weight updates every request  
**Answer:** A, B, C  
**Why:** D is training, not prompting.

### Q33 [RAI] MCQ
Privacy and security principle most directly concerns:
- A. Vector dimensions
- B. Data handling and access controls
- C. Learning rate
- D. Caption quality  
**Answer:** B  
**Why:** Privacy/security governs data protection.

### Q34 [CV] MCQ
Classifying whether an image is "defective" or "normal" is:
- A. OCR
- B. Classification
- C. Detection only
- D. Translation  
**Answer:** B  
**Why:** Output is category label.

### Q35 [ML] MCQ
Underfitting usually means:
- A. Model too complex
- B. Model too simple for pattern complexity
- C. Too much data
- D. Perfect generalization  
**Answer:** B  
**Why:** Underfitting misses key patterns.

### Q36 [NLP] Scenario
You need a multilingual support bot with translation and sentiment triage. Pick two core capabilities:
- A. Translation
- B. Sentiment analysis
- C. Object detection
- D. OCR only  
**Answer:** A, B  
**Why:** Matches multilingual + triage needs.

### Q37 [GenAI] MCQ
Which service is central for GPT-style model deployment in Azure?
- A. Azure AI Vision
- B. Azure OpenAI Service
- C. Azure DNS
- D. Azure Batch  
**Answer:** B  
**Why:** Azure OpenAI hosts LLM endpoints with enterprise controls.

### Q38 [AI] MCQ
AI workload selection should start with:
- A. Most expensive model
- B. Clear business problem and success criteria
- C. First service you see
- D. Ignoring data quality  
**Answer:** B  
**Why:** Problem-first design drives valid solution choice.

### Q39 [ML] Scenario
Dataset is 95% class A and 5% class B. Best metric strategy:
- A. Accuracy only
- B. Precision/recall/F1 by class
- C. Ignore confusion matrix
- D. Use RMSE only  
**Answer:** B  
**Why:** Class imbalance hides failure under plain accuracy.

### Q40 [RAI][GenAI] MCQ
Which is best practice before production launch of a GenAI app?
- A. Disable safety filters for realism
- B. Conduct abuse testing and set safety policies
- C. Never log anything
- D. Skip human review workflows  
**Answer:** B  
**Why:** Safety testing and policy controls are mandatory.

## Practice strategy

### Use Microsoft practice assessment effectively
1. **Pass 1 (diagnostic):** untimed, identify weak objectives.
2. **Pass 2 (timed):** simulate exam pace and pressure.
3. **Pass 3 (targeted):** redo only weak domain questions.
4. **Spaced repetition:** revisit misses after 24 hours, then 72 hours.
5. **Error log:** keep a short list of "why I missed this" patterns.

### Readiness checklist
You are exam-ready when you can explain each item in 30 seconds:
- Regression vs classification vs clustering.
- Feature vs label.
- Precision vs recall and when each matters.
- Confusion matrix terms (TP/TN/FP/FN).
- Overfitting and one mitigation.
- Classification vs object detection.
- OCR vs image classification use cases.
- Sentiment vs key phrase vs entity extraction.
- Token, embedding, prompt, context window.
- Grounding and RAG difference from fine-tuning.
- Responsible AI principles and one concrete action per principle.

### Final 24-hour review plan
- **T-24h:** One timed practice pass, review only wrong answers.
- **T-18h:** Read summary notes for five skill domains.
- **T-12h:** Light glossary skim, focus metrics and GenAI terms.
- **T-8h:** Confirm logistics (ID, schedule, environment, internet).
- **T-2h:** Stop cramming. Do a short confidence check and rest.

## Resources

### Official Microsoft resources (primary)
- Certification page:  
  https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
- Study guide (skills measured):  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900
- Practice assessments:  
  https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications
- Register/schedule exam:  
  https://learn.microsoft.com/en-us/credentials/certifications/register-schedule-exam
- Microsoft Learn training collections (from cert page and linked modules).

### Optional community resources (secondary)
- YouTube AI-900 cram videos from reputable instructors/channels (optional, verify date).
- Community question banks (optional, use for style exposure, not authoritative truth).
- Blog walkthroughs for Azure AI service overviews (optional, cross-check with Learn docs).

---

If you update this plan after Microsoft revises the study guide, prioritize the official study guide skill domains first, then refresh sample questions and glossary mappings.
