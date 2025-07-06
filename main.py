# main.py

from scraper.web_scraper import get_page_content
from summarizer.openai_summarizer import summarize_with_openai
from summarizer.ollama_summarizer import summarize_with_ollama
from eval.evaluator import evaluate_summaries


def run_dual_llm_pipeline(url):
    print(f"\nScraping content from: {url}")
    content = get_page_content(url)
    if not content:
        print("Failed to retrieve or parse content.")
        return

    print("\nGenerating summary with OpenAI...")
    openai_summary = summarize_with_openai(content)

    print("\nGenerating summary with Ollama...")
    ollama_summary = summarize_with_ollama(content)

    print("\nEvaluating summaries with GPT-4...")
    result = evaluate_summaries(openai_summary, ollama_summary, content)

    print("\n==============================")
    print(f"Winning Model: {result['winner']}")

    print("\nReasoning:")
    print(result.get('justification', 'No reasoning provided.'))

    print("\n--- OpenAI Summary ---")
    print(openai_summary)

    print("\n--- Ollama Summary ---")
    print(ollama_summary)
    print("==============================")


if __name__ == "__main__":
    test_url = input("Enter the URL to summarize: ").strip()
    run_dual_llm_pipeline(test_url)
