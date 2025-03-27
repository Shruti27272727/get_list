import re
from typing import List, Dict

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filter papers with non-academic (pharma/biotech) affiliations"""
    pharma_keywords = ['pharma', 'biotech', 'ltd', 'inc', 'corp', 'gmbh', 'labs']

    filtered = []

    for paper in papers:
        non_academic_authors = []
        company_affiliations = []

        for author in paper.get("Authors", []):
            affiliation = author.get("affiliation", "")
            email = author.get("email", "")

            if any(kw in affiliation.lower() for kw in pharma_keywords):
                non_academic_authors.append(author.get("name"))
                company_affiliations.append(affiliation)

        if non_academic_authors:
            filtered.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "PublicationDate": paper["PublicationDate"],
                "NonAcademicAuthors": "; ".join(non_academic_authors),
                "CompanyAffiliations": "; ".join(company_affiliations),
                "CorrespondingAuthorEmail": email
            })

    return filtered
