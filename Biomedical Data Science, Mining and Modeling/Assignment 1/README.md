# Description:
This assignment was for Yale University's Biomedical Data Science, Mining and Modeling course. Given short DNA sequences labeled as "binds a transcription factor" (1) or "does not" (0), this notebook builds two independent classifiers (SVM and neural network) and interprets what each one learned.

# Skills Demonstrated:
## Genomics / domain knowledge
- Framing protein–DNA binding (ChIP-seq / transcription factor binding site discovery) as a supervised sequence classification problem.
- One-hot and k-mer encoding schemes for categorical biological sequence data.
- Reading and reasoning about ENCODE-derived ChIP-seq / DNase-seq datasets, including positive/negative peak-calling logic (IDR peaks vs. DNase accessibility controls).
## Classical machine learning
- Feature engineering from raw sequence (k-mer frequency vectors, choice of k).
- GridSearchCV / RandomizedSearchCV with 5-fold cross-validation for model selection across kernels (linear/rbf/poly/sigmoid) and regularization strength.
- Held-out test set evaluation (accuracy) and permutation feature importance for model interpretability.
## Deep learning
- Custom nn.Module CNN architecture design (Conv1D → MaxPool → Flatten → Dense → Sigmoid), including manually working out output dimensions after conv/pool layers.
- Hand-written training loop: forward pass, loss computation, backprop, optimizer step.
- Train/validation/test split discipline and per-epoch loss/accuracy tracking to diagnose overfitting.
- Confusion matrix evaluation
- Model interpretability: gradient × input saliency maps and sequence logo visualization (logomaker) to localize the exact bases driving a prediction.
- Systematic hyperparameter ablation: loss function (BCE vs. MSE vs. hinge), number of conv filters (1–64), kernel size (1–32), each evaluated via precision/recall curves rather than accuracy alone.
- Reasoned, written justification for loss function choice.
## General software / ML engineering
- Reproducible pipelines with fixed random seeds.
- Clean separation of data loading, preprocessing, modeling, and evaluation code.