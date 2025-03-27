import requests
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_papers(query: str, debug: bool = False) -> List[Dict]:
    """Fetch papers from PubMed API"""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 100,  # Number of results
        "retmode": "json"
    }

    response = requests.get(f"{BASE_URL}esearch.fcgi", params=params)
    response.raise_for_status()

    ids = response.json().get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []

    id_str = ",".join(ids)
    summary_response = requests.get(f"{BASE_URL}esummary.fcgi", params={"db": "pubmed", "id": id_str, "retmode": "json"})
    summary_response.raise_for_status()

    data = summary_response.json().get("result", {})
    papers = []

    for pid in ids:
        paper = data.get(pid, {})
        authors = paper.get("authors", [])
        
        papers.append({
            "PubmedID": pid,
            "Title": paper.get("title"),
            "PublicationDate": paper.get("pubdate"),
            "Authors": authors
        })

    if debug:
        print(f"Fetched {len(papers)} papers.")
    
    return papers
