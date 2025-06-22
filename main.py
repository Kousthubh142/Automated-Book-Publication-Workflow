import os
import json
from scrape.static_scraper import scrape_chapter
from ai_agents.writer_agent import spin_chapter
from ai_agents.reviewer_agent import review_chapter
from db.chromadb_handler import store_version
from db.rl_search import reward_version

def generate_doc_id(book: str, chapter: int) -> str:
    return f"{book.lower().replace(' ', '_')}_chapter_{chapter:02d}"

def main():
    # Step 1: Scrape
    chapter_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    print("[1] Scraping original chapter...")
    original_text = scrape_chapter(chapter_url)

    # Step 2: Spin
    print("[2] Spinning chapter using Gemini...")
    spun_text = spin_chapter(original_text)

    # Step 3: Review
    print("[3] Reviewing spun chapter...")
    reviewed_text = review_chapter(spun_text, original_text)

    # Step 4: Save data to temp JSON for Streamlit UI
    print("[4] Launching human review interface...")
    os.makedirs("interface", exist_ok=True)
    with open("interface/temp_review_data.json", "w", encoding="utf-8") as f:
        json.dump({
            "original": original_text,
            "spun": spun_text,
            "reviewed": reviewed_text
        }, f)

    print("\n👉 Now run the following in a new terminal to open the interface:\n")
    print("   streamlit run interface/human_review_interface.py\n")

    print("⚠️  After saving the final version in the UI, press ENTER here to continue...")
    input()

    # Step 5: Load finalized version and store
    finalized_path = input("Enter the name of the finalized file (from final_output/): ")
    with open(f"final_output/{finalized_path}", "r", encoding="utf-8") as f:
        finalized_text = f.read()

    # Step 6: Store in ChromaDB
    doc_id = generate_doc_id("Gates of Morning", 1)
    store_version(doc_id, finalized_text, {"chapter": 1, "book": "Gates of Morning"})
    reward_version(doc_id)

    print(f"\n✅ Finalized version stored in ChromaDB with doc ID: {doc_id}")
    print("🎉 Workflow complete!")

if __name__ == "__main__":
    main()
