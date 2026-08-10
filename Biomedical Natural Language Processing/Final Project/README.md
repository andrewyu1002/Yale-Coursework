# Description:
LLMs used in clinical contexts carry real risk: they can hallucinate fluent-sounding but factually wrong answers, and their static training data quickly falls behind evolving medical knowledge. This project investigates RAG as a way to mitigate both problems, and compares it against RAFT, a variant that also fine-tunes the model to make better use of retrieved context.

The project scoped itself to primary care, the highest-volume, broadest-coverage point of contact in healthcare, using the MedMCQA dataset (medical entrance exam-style multiple-choice questions) filtered to primary-care-relevant subjects (Medicine, Pharmacology, Microbiology, Social & Preventive Medicine, ENT, Psychiatry, Orthopaedics, Skin), with an 80/20 train/test split.

System architecture
- Base model: BioMistral-7B (a Mistral-7B variant pretrained on PubMed Central Open Access text), loaded in 4-bit quantization to fit in a Google Colab environment.
- Retrieval corpus: StatPearls, a lightweight, broad-coverage medical knowledge base from NCBI.
- Retrieval pipeline: StatPearls was chunked using the MedRAG toolkit and encoded with MedCPT. A FAISS index was built over the embeddings for fast similarity search. At query time: MedCPT encodes the question → FAISS retrieves the most relevant StatPearls chunks → those chunks are added as context for the LLM's response.
- Fine-tuning: LoRA adapters were used for efficient fine-tuning of the quantized base model.

# Skills Demonstrated:
Retrieval-Augmented Generation (RAG) & RAFT
- Designing and implementing a full RAG pipeline: corpus chunking, dense embedding, vector indexing, and retrieval-augmented prompting.
- Implementing Retrieval-Augmented Fine-Tuning (RAFT) to train a model to better utilize retrieved context, and evaluating its marginal benefit over standard RAG.
- Comparative experimental design across multiple model/retrieval conditions.

LLM Fine-Tuning & Efficient Training
- Parameter-efficient fine-tuning (LoRA) of a 7B-parameter LLM under hardware constraints.
- 4-bit quantization to fit large models in memory-limited environments (Google Colab).
- Monitoring training loss and detecting overtraining via epoch-level checkpoint comparison.

Information Retrieval for Biomedical NLP
- Building a dense retrieval system with domain-specific encoders (MedCPT) and FAISS for efficient similarity search.
- Working with domain corpora (StatPearls) and open biomedical LLMs (BioMistral-7B).

Experimentation & Scientific Analysis
- Designing a multi-arm study (5 conditions) with a clear evaluation metric (accuracy) and consistent test set.
- Diagnosing failure modes through qualitative error analysis (e.g., identifying that retrieval was "topically" but not "specifically" relevant).
- Drawing evidence-based conclusions about where a system's remaining errors originate (retrieval quality vs. reasoning) and proposing targeted next steps (pre-retrieval and inference-time chain-of-thought).
- Communicating technical results clearly through data visualization, a written report, and a presentation.