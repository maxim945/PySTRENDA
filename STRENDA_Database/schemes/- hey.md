```mermaid
classDiagram
    ProteinSequence *-- ProteinDatabase
    ProteinSequence *-- Organism
    DNASequence *-- ProteinSequence
    DNASequence *-- DNADatabase
    DNASequence *-- Organism
    StandardNumberingScheme *-- ProteinSequence
    Position *-- ProteinSequence
    Annotation *-- ProteinSequence
    
    class ProteinSequence {
        +string protein_sequence_id
        +string name
        +string amino_acid_sequence
        +ProteinDatabase protein_database_name
        +Organism protein_organism_id
    }
    
    class DNASequence {
        +ProteinSequence protein_sequence_id
        +string dna_sequence_id
        +string nucleotide_sequence
        +DNADatabase dna_database_id
        +Organism dna_organism_id
    }
    
    class Organism {
        +string organism_name
        +string ncbi_taxonomy_id
    }
    
    class ProteinDatabase {
        +integer database
        +integer link_to_database
    }
    
    class DNADatabase {
        +integer database
        +integer link_to_database
    }
    
    class StandardNumberingScheme {
        +ProteinSequence protein_sequence_id
        +integer standard_numering_scheme_id
        +string standard_numering_scheme_name
        +string standard_numering_scheme
    }
    
    class Position {
        +integer position_id
        +ProteinSequence protein_sequence_id
        +integer standard_numbering_scheme_id
        +integer annotation_id
    }
    
```