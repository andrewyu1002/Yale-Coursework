import requests
import time
import xml.etree.ElementTree as ET
import json

def get_papers(query):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmax=1000&retmode=xml"
    r = requests.get(url)
    time.sleep(1)
    return r.content

alzheimers_2023 = get_papers("Alzheimers+AND+2023[pdat]")
cancer_2023 = get_papers("cancer+AND+2023[pdat]")

def pubmed_ids(data):
    root = ET.fromstring(data)
    return [id_element.text for id_element in root.findall(".//Id")]

alzheimers_ids = pubmed_ids(alzheimers_2023)
cancer_ids = pubmed_ids(cancer_2023)

def get_metadata(ids):
    all_metadata = []
    batch_size = 200
    for i in range(0, len(ids), batch_size):
        batch_ids = ids[i:i + batch_size]
        ids_string = ",".join(batch_ids)
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids_string}&retmode=xml"
        r = requests.get(url)
        time.sleep(1)
        all_metadata.append(r.content)
    return all_metadata

alzheimers_metadata = get_metadata(alzheimers_ids)
cancer_metadata = get_metadata(cancer_ids)

def extract_metadata(data, query_type):
    metadata = {}
    for batch in data:
        root = ET.fromstring(batch)
        for pubmed_article in root.findall(".//PubmedArticle"):
            pmid = pubmed_article.find("MedlineCitation/PMID").text

            title_element = pubmed_article.find("MedlineCitation/Article/ArticleTitle")
            if title_element is not None:
                title = ET.tostring(title_element, method="text", encoding="unicode")
            else:
                title = "No title available"

            abstract_element = pubmed_article.find("MedlineCitation/Article/Abstract/AbstractText")
            if abstract_element is not None:
                abstract_text = ET.tostring(abstract_element, method="text", encoding="unicode")
            else:
                abstract_text = "No abstract available"

            metadata[pmid] = {
                "ArticleTitle": title,
                "AbstractText": abstract_text,
                "query": query_type
            }
    return metadata

alzheimers_metadata_json = extract_metadata(alzheimers_metadata, "Alzheimer")
cancer_metadata_json = extract_metadata(cancer_metadata, "cancer")

with open('problem_set_2/pubmed_metadata.json', 'w') as f:
    json.dump({**alzheimers_metadata_json, **cancer_metadata_json}, f, indent=4)

overlap_ids = set(alzheimers_ids) & set(cancer_ids)
print("Overlapping PubMed IDs for Alzheimers and cancer:", overlap_ids)