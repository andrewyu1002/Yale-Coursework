# Description:
A text classification assignment that predicts which section of a scientific abstract a sentence belongs to (Background, Methods, Results, or Conclusions) using both classical machine learning and transformer-based deep learning approaches. 

Two modeling approaches are implemented and benchmarked against each other:
- Feature-based ML: TF-IDF vectorization combined with classical classifiers (Linear SVC, Random Forest)
- Deep learning with pretrained transformers: Fine-tuning BiomedBERT using the Hugging Face Trainer API

# Skills Demonstrated:
- Feature engineering with TF-IDF vectorization for text data.
- Training and evaluating classical ML classifiers (Linear SVC, Random Forest) with scikit-learn.
- Fine-tuning pretrained transformer models (BERT-family) for sequence classification.
- Working with domain-specific pretrained models (BiomedBERT) for biomedical NLP.
- Model evaluation and comparison using train/test/validation splits and accuracy metrics.