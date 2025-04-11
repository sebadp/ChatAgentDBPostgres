import json
import re
import streamlit as st


def parse_dispatch_result(dispatch_result: str) -> tuple[str, str, str]:
    """
    Parses the result from the dispatcher LLM.
    Returns (reasoning, action, explanation).
    If the result is not valid JSON, attempts to extract information via regex or defaults.
    """
    try:
        # Try to find JSON content in the response (sometimes models wrap JSON in markdown or other text)
        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', dispatch_result, re.DOTALL)
        if json_match:
            # If there's JSON within code blocks, try to parse that
            data = json.loads(json_match.group(1))
        else:
            # Try to parse the whole response as JSON
            data = json.loads(dispatch_result)

        reasoning = data.get("reasoning", "")
        action = data.get("action", "database_query")
        explanation = data.get("explanation", "")

    except json.JSONDecodeError:
        # If JSON parsing fails, try to extract information using regex
        # Look for action pattern
        action_match = re.search(r'"action":\s*"(database_query|memory_lookup|direct_response)"', dispatch_result)
        action = action_match.group(1) if action_match else "database_query"

        # Extract potential reasoning
        reasoning = dispatch_result
        explanation = "Content extracted from non-JSON response."

        # Don't show warning to user - handle gracefully
        if st.session_state.get("show_reasoning", False):
            st.info("Note: Planner output was not formatted as valid JSON, but I was able to process it.")

    return reasoning, action, explanation