# Description
This assignment was for Yale University's Biomedical Data Science, Mining and Modeling course. This assignment covers protein
structural geometry, deep generative modeling for medical imaging, and single-cell RNA-seq analysis, highlighting the ability to work with classical structural bioinformatics, deep learning, and single-cell genomics analysis.

# Skills Demonstrated
## Protein Backbone & Side-Chain Geometry
- Implementing dihedral (torsion) angle calculation.
- Applying this to compute backbone dihedrals (φ, ψ) and side-chain dihedrals (χ1) for threonine residues.
- Producing a Ramachandran plot and a distribution plot of the χ1 side-chain dihedral angle.
## Conditional Variational Autoencoder (PyTorch) on DermaMNIST Dataset
- Data pipeline: torchvision/medmnist dataset loading, transforms, DataLoader construction for train/val/test splits.
- Building a convolutional encoder/decoder architecture in PyTorch.
- Implementing class conditioning by concatenating one-hot labels into the latent representation (CVAE).
- Implementing the reparameterization trick (mu + std * eps) to allow backpropagation through a stochastic sampling step
- Constructing the full VAE loss (reconstruction loss + KL divergence loss + β).
- Model evaluation: reconstruction visualization, and dimensionality reduction of the learned latent space with UMAP, colored by class label, to qualitatively assess whether the representation is meaningful.
## Single-Cell RNA-seq Analysis (Scanpy)
- Simulating and comparing Poisson vs. Negative Binomial count distributions.
- Loading 10x Genomics data and performing standard QC.
- Standard normalization pipeline: total-count normalization, log1p transform, highly-variable-gene selection, scaling/clipping.
- Dimensionality reduction and clustering: PCA → kNN graph → UMAP embedding → Leiden clustering.
- Biological interpretation: using canonical immune marker genes to annotate clusters with cell-type labels.