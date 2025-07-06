# eval/gpt_judge.py

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import logging
from dotenv import load_dotenv

load_dotenv()  
logger = logging.getLogger(__name__)


def gpt_based_evaluation(summary1: str, summary2: str, article: str) -> dict:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_template(
        """
    You are an expert evaluator. Compare two summaries of a news article and decide which one better captures the content.

    --- Article ---
    {article}

    --- Summary 1 ---
    {summary1}

    --- Summary 2 ---
    {summary2}

    Reply in JSON format like this:
    {{
    "winner": "Summary 1" | "Summary 2" | "Tie",
    "justification": "<reason>"
    }}
    """
    )

    response_schema = [
        ResponseSchema(name="winner", description="Better summary: Summary 1, Summary 2, or Tie"),
        ResponseSchema(name="justification", description="Explanation for the decision")
    ]

    parser = StructuredOutputParser.from_response_schemas(response_schema)
    chain = prompt | llm | parser

    try:
        result = chain.invoke({
            "article": article,
            "summary1": summary1,
            "summary2": summary2
        })
        return result
    except Exception as e:
        logger.error(f"GPT-based evaluation failed: {e}")
        return {
            "winner": "Tie",
            "justification": f"Evaluation failed due to error: {str(e)}"
        }
