# PyEED Data Model

PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles.

### ProteinSequence

- __protein_sequence_id__
  - Type: string
  - Description: Presented protein sequence
- __name__
  - Type: string
  - Description: Systematic name of the protein.
- __amino_acid_sequence__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __protein_database_name__
  - Type: [ProteinDatabase](#ProteinDatabase)
  - Description: Data base ID
- __protein_organism_id__
  - Type: [Organism](#Organism)
  - Description: Corresponding organism 


### DNASequence


- __protein_sequence_id__
  - Type: [ProteinSequence](#ProteinSequence)
  - Description: Presented protein sequence
- __dna_sequence_id__
  - Type: string
  - Description: Reference to the Translated DNA from the matching Protein sequence
- __nucleotide_sequence__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __dna_database_id__
  - Type: [DNADatabase](#DNADatabase)
  - Description: Data base ID
- __dna_organism_id__
  - Type: [Organism](#Organism)
  - Description: NCBI Taxonomy ID to identify the organism
  - 
### Organism

- __organism_name__
  - Type: string
  - Description: Organism name
- __ncbi_taxonomy_id__
  - Type: string
  - Description: NCBI Taxonomy ID to identify the organism
  - hey

### ProteinDatabase

- __database__
  - Type: integer
  - Description: Position in the sequence where the domain starts
- __link_to_database__
  - Type: integer
  - Description: Position in the sequence where the domain ends

### DNADatabase

- __database__
  - Type: integer
  - Description: Position in the sequence where the domain starts
- __link_to_database__
  - Type: integer
  - Description: Position in the sequence where the domain ends

### StandardNumberingScheme

- __protein_sequence_id__
  - Type: [ProteinSequence](#ProteinSequence)
  - Description: Presented protein sequence
- __standard_numering_scheme_id__
  - Type: integer
  - Description: the id of the scheme
- __standard_numering_scheme_name__
  - Type: string
  - Description: the name of each standard numbering
- __standard_numering_scheme__
  - Type: string
  - Description: the numbering scheme for each sequence


### Position

- __position_id__
  - Type: integer
  - Description: Equivalent position in the reference sequence
- __protein_sequence_id__
  - Type: [ProteinSequence](#ProteinSequence)
  - Description: Position that is equivalent to the reference sequence position that is also given
- __standard_numbering_scheme_id__
  - Type: integer
  - Description: Position that is equivalent to the reference sequence position that is also given
- __annotation_id__
  - Type: integer
  - Description: Function that is found in the annotated amino acid or sub-sequence

  
### Annotation

- __protein_sequence_id__
  - Type: [ProteinSequence](#ProteinSequence)
  - Description: Start position of the annotation. A single start position without an end corresponds to a single amino acid
- __start_position__
  - Type: integer
  - Description: Optional end position if the annoation contains more than a single amino acid.
- __end_position__
  - Type: integer
  - Description: Optional end position if the annoation contains more than a single amino acid.
- __function__
  - Type: string
  - Description: Function that is found in the annotated amino acid or sub-sequence

 
