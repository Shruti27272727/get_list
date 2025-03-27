import csv
from typing import List, Dict

def export_to_csv(papers: List[Dict], filename: str):
    """Export paper details to CSV"""
    headers = ["PubmedID", "Title", "PublicationDate", "NonAcademicAuthors", "CompanyAffiliations", "CorrespondingAuthorEmail"]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for paper in papers:
            writer.writerow(paper)
