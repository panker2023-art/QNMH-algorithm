# Product Context

## User Stories & Needs
- **Researchers/Biologists**: Need a standardized pipeline to process snRNA-seq data from different mouse genetic backgrounds and humans.
- **Translational Scientists**: Require the Quantitative Network Motif Homology (QNMH) algorithm to compute a structural isomorphism score ($S_{iso}$) to filter out "pseudo-drugs" that only work in specific genetic backgrounds.
- **Pharmacologists**: Will use the Precise Risk Index (PRI) to prioritize candidate targets/drugs by evaluating their cross-strain robustness.

## High-level Outputs
1. **GDI Matrix Preprocessor**: An automated script/API that inputs single-cell sequencing & spatial transcriptomics and normalizes them for network construction.
2. **GRN Modeler**: Reconstructs gene regulatory networks for each subset (e.g. disease-associated microglia).
3. **QNMH Core Engine**: Computes edge-weight topological isomorphism, generating $S_{iso}$.
4. **PRI Calculator**: Computes risk indices combining target connectivity and genetic background robustness.

## Key Success Metrics
- Differentiate AD vs non-AD (e.g., ALS) GRNs accurately.
- Accurately predict shielding genes (*Grn*) for future AAV-CRISPR validation in B6 mice.
