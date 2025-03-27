import pytest
from get_papers.api import fetch_pubmed_papers

def test_fetch_pubmed_papers():
    papers = fetch_pubmed_papers("cancer AND pharma", debug=True)
    assert len(papers) > 0
    assert "PubmedID" in papers[0]
