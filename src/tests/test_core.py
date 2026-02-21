import pytest
import networkx as nx
from src.core.qnmh.nx_impl import NetworkXQNMHSolver
from src.core.pri.calculator import calculate_pri

def test_qnmh_solver_basic():
    solver = NetworkXQNMHSolver()
    
    # Create simple dummy graphs
    G1 = nx.Graph()
    G1.add_edges_from([(1,2), (2,3), (3,1)]) # A triangle
    
    G2 = nx.Graph()
    G2.add_edges_from([(4,5), (5,6), (6,4)]) # Another triangle
    
    # Since they are isomorphic structurally (clustering coeff 1.0 for both),
    # S_iso should be 1.0
    s_iso = solver.calculate_homology(G1, G2)
    assert s_iso == 1.0

def test_pri_calculator():
    # Test high robustness, no penalty
    score1 = calculate_pri(qnmh_score=0.9, genetic_robustness_score=0.8, toxicity_penalty=0.0)
    assert score1 == (0.9 * 0.6) + (0.8 * 0.4)
    
    # Test penalty
    score2 = calculate_pri(qnmh_score=0.9, genetic_robustness_score=0.8, toxicity_penalty=0.5)
    assert score2 == ((0.9 * 0.6) + (0.8 * 0.4)) - 0.5
    
    # Test bounding (should not go below 0)
    score3 = calculate_pri(qnmh_score=0.1, genetic_robustness_score=0.1, toxicity_penalty=0.9)
    assert score3 == 0.0
