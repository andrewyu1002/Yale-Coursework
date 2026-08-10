# Description:
A project that fine-tunes BERT for token-level named entity recognition (NER), identifying chemical entities in PubMed abstracts using BIO tagging.

This project builds a full BioNER pipeline: taking raw BIO-formatted biomedical text, preparing it for a transformer model, fine-tuning bert-base-cased with a token-classification head, and systematically tuning hyperparameters to maximize performance. The end goal is to automatically detect and tag chemical entity mentions (e.g., drug names) within scientific abstract text at the token level.

The pipeline consists of the following:
1. Data preparation: Parsed BIO-formatted train/dev/test TSV files into token/label lists and wrapped them into Hugging Face Dataset objects.
2. Subword alignment: BERT uses subword tokenization, so BIO labels were aligned to the first subword piece of each token.Special tokens and subsequent subword pieces masked (-100) so they don't contribute to the loss.
3. Model fine-tuning: Loaded a pretrained bert-base-cased model with a token-classification head and fine-tuned it using the Hugging Face Trainer API.
4. Evaluation: Used seqeval to compute precision, recall, F1, and accuracy at each checkpoint, selecting the best model by validation F1.
5. Hyperparameter tuning: Independently swept learning rate (1e-5, 2e-5, 3e-5) and number of epochs (2, 3, 5) on the dev set, then combined the best-performing values for a final training run.
6. Error analysis: Broke down per-label precision (O, B, I) on the dev set to characterize where the model struggles.

# Skills Demonstrated:
NLP & Sequence Labeling
- Understanding and implementing BIO tagging for named entity recognition.
- Handling the subword-to-word label alignment problem inherent to transformer tokenizers.
- Fine-tuning a pretrained transformer (bert-base-cased) with a token-classification head for a downstream sequence labeling task.
Model Training & Evaluation
- Building an end-to-end Hugging Face training pipeline.
- Implementing a custom compute_metrics function using seqeval for entity-level precision, recall, F1, and token-level accuracy.
- Selecting model checkpoints based on validation F1 rather than loss alone, and understanding why a single metric (e.g., accuracy) can be misleading on imbalanced sequence-labeling tasks.
Experimentation & Hyperparameter Tuning
- Systematic hyperparameter search (independent sweep over learning rate and epoch count, followed by a combined final run).
- Documenting and justifying a tuning strategy based on validation results.
Error Analysis
- Per-label precision breakdown to diagnose specific model weaknesses (e.g., harder performance on multi-token entities vs. single-token entities).
- Confusion analysis between true and predicted BIO labels to identify systematic error patterns.