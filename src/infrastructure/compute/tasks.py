from typing import Dict, Any
from src.core.qnmh.nx_impl import NetworkXQNMHSolver
from src.core.pri.calculator import calculate_pri

def run_qnmh_analysis(matrix_file_path: str, reference_network_path: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Wrapper function to be run in a separate process.
    Instantiates the solver, loads data, and calculates QNMH and PRI.
    """
    solver = NetworkXQNMHSolver()
    
    try:
        # Load networks
        source_net = solver.load_network(matrix_file_path)
        ref_net = solver.load_network(reference_network_path)
        
        # Calculate Homology (QNMH)
        qnmh_score = solver.calculate_homology(source_net, ref_net)
        
        # Extract motifs (dummy implementation for prototype)
        motifs = solver.extract_motifs(source_net)
        
        # Calculate PRI
        # In a real scenario, robustness and toxicity would be derived from other data
        robustness = metadata.get("genetic_robustness", 0.8) if metadata else 0.8
        toxicity = metadata.get("toxicity_penalty", 0.1) if metadata else 0.1
        
        pri_score = calculate_pri(qnmh_score, robustness, toxicity)
        
        return {
            "qnmh_score": qnmh_score,
            "pri_score": pri_score,
            "motifs": motifs,
            "nodes_source": len(source_net),
            "nodes_ref": len(ref_net)
        }
    except Exception as e:
        raise RuntimeError(f"QNMH analysis failed: {str(e)}")
