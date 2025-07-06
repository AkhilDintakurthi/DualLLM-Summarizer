# eval/evaluator.py

import logging
from dotenv import load_dotenv
from eval.gpt_judge import gpt_based_evaluation 

logger = logging.getLogger(__name__)
load_dotenv()


def evaluate_summaries(summary1: str, summary2: str, article_text: str) -> dict:
    logger.info("Evaluating summaries using GPT judge...")
    return gpt_based_evaluation(summary1, summary2, article_text)
