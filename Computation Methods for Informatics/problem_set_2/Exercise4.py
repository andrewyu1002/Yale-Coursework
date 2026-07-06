from transformers import AutoTokenizer, AutoModel
import json
import tqdm
from sklearn import decomposition
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('allenai/specter')
model = AutoModel.from_pretrained('allenai/specter')

with open('problem_set_2/pubmed_metadata.json', 'r') as f:
    papers = json.load(f)

# we can use a persistent dictionary (via shelve) so we can stop and restart if needed
# alternatively, do the same but with embeddings starting as an empty dictionary
embeddings = {}
for pmid, paper in tqdm.tqdm(papers.items()):
    data = [paper["ArticleTitle"] + tokenizer.sep_token + paper.get("AbstractText")]
    inputs = tokenizer(
        data, padding=True, truncation=True, return_tensors="pt", max_length=512
    )
    result = model(**inputs)
    # take the first token in the batch as the embedding
    embeddings[pmid] = result.last_hidden_state[:, 0, :].detach().numpy()[0]

# turn our dictionary into a list
embeddings = [embeddings[pmid] for pmid in papers.keys()]

pca = decomposition.PCA(n_components=3)
embeddings_pca = pd.DataFrame(
    pca.fit_transform(embeddings),
    columns=['PC0', 'PC1', 'PC2']
)
embeddings_pca["query"] = [paper["query"] for paper in papers.values()]

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(data=embeddings_pca, x='PC0', y='PC1', hue='query')
plt.title('PC0 vs PC1')
plt.xlabel('PC0')
plt.ylabel('PC1')

plt.subplot(1, 3, 2)
sns.scatterplot(data=embeddings_pca, x='PC0', y='PC2', hue='query')
plt.title('PC0 vs PC2')
plt.xlabel('PC0')
plt.ylabel('PC2')

plt.subplot(1, 3, 3)
sns.scatterplot(data=embeddings_pca, x='PC1', y='PC2', hue='query')
plt.title('PC1 vs PC2')
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.tight_layout()
plt.show()