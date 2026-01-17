def build_evidence(results):
    if not results or (
        isinstance(results, dict)
        and not results.get("text")
        and not results.get("image")
    ):
        return ["No relevant patient history found for this query."]

    evidence = []

    if isinstance(results, dict):
        for modality, items in results.items():
            for i, r in enumerate(items):
                payload = r.payload
                evidence.append(
                    f"[{modality.upper()}] {payload.get('summary')} "
                    f"(date: {payload.get('date')}, category: {payload.get('category')})"
                )
    else:
        for i, r in enumerate(results):
            payload = r.payload
            evidence.append(
                f"{payload.get('summary')} "
                f"(date: {payload.get('date')}, category: {payload.get('category')})"
            )

    return evidence



def build_reasoning(query, evidence):
    """
    Build a traceable reasoning explanation
    """
    if not evidence:
        return "No relevant medical history found for this query."

    reasoning = []
    reasoning.append(f"Query: {query}")
    reasoning.append("")

    reasoning.append("Relevant evidence retrieved:")
    for e in evidence:
        reasoning.append(f"- {e}")

    reasoning.append("")
    reasoning.append(
        "Conclusion: Based on the retrieved patient history above, "
        "the system highlights patterns relevant to the query. "
        "This output is evidence-based and does not provide diagnosis."
    )

    return "\n".join(reasoning)
