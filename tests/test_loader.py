from app.retrieval.catalog_loader import CatalogLoader


def main():
    loader = CatalogLoader()

    catalog = loader.load_catalog()
    print(f"Total assessments: {len(catalog)}")
    print("\nFirst Assessment:\n")
    print(catalog[0])

    print("\nEmbedding Text:\n")
    print(catalog[0].embedding_text())

if __name__ == "__main__":
    main()