from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple

class QNMHSolver(ABC):
    """Abstract interface for QNMH (Quantitative Network Motif Homology) calculation."""
    
    @abstractmethod
    def load_network(self, file_path: str) -> Any:
        """Load network from file."""
        pass
    
    @abstractmethod
    def calculate_homology(self, source_network: Any, reference_network: Any) -> float:
        """
        Calculate structural homology between source and reference networks.
        Returns a score S_iso between 0 and 1.
        """
        pass
    
    @abstractmethod
    def extract_motifs(self, network: Any, motif_size: int = 3) -> Dict[str, int]:
        """Extract network motifs and their frequencies."""
        pass
