import argparse
from get_papers.api import fetch_pubmed_papers
from get_papers.parser import filter_non_academic_authors
from get_papers.exporter import export_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech authors.")
    parser.add_argument("query", type=str, help="PubMed search query.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file", default="output.csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    try:
        papers = fetch_pubmed_papers(args.query, args.debug)
        filtered_papers = filter_non_academic_authors(papers)

        if not filtered_papers:
            print("No matching papers found.")
        else:
            export_to_csv(filtered_papers, args.file)
            print(f"Results saved to {args.file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
