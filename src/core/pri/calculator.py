def calculate_pri(qnmh_score: float, genetic_robustness_score: float, toxicity_penalty: float = 0.0) -> float:
    """
    Calculate the Precision Risk Index (PRI).
    
    Args:
        qnmh_score (float): S_iso score from QNMH algorithm (0.0 to 1.0)
        genetic_robustness_score (float): Score indicating stability across genetic backgrounds (0.0 to 1.0)
        toxicity_penalty (float): Penalty for predicted off-target or toxicity effects (0.0 to 1.0)
        
    Returns:
        float: Computed PRI score. Higher is better.
    """
    # PRI formulation: (Network Homology * Robustness) - Toxicity
    # Ensure values are bounded
    
    qnmh_score = max(0.0, min(1.0, qnmh_score))
    robustness = max(0.0, min(1.0, genetic_robustness_score))
    penalty = max(0.0, min(1.0, toxicity_penalty))
    
    # Simple linear combination for prototype
    base_score = (qnmh_score * 0.6) + (robustness * 0.4)
    final_score = max(0.0, base_score - penalty)
    
    return final_score
