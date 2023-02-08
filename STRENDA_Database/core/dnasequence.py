import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .dnadatabase import DNADatabase
from .organism import Organism
from .proteinsequence import ProteinSequence


@forge_signature
class DNASequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dnasequenceINDEX"),
        xml="@id",
    )
    protein_sequence_id: Optional[ProteinSequence] = Field(
        description="Presented protein sequence",
        default=None,
    )

    dna_sequence_id: Optional[str] = Field(
        description=(
            "Reference to the Translated DNA from the matching Protein sequence"
        ),
        default=None,
    )

    nucleotide_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    dna_database_id: Optional[DNADatabase] = Field(
        description="Data base ID",
        default=None,
    )

    dna_organism_id: Optional[Organism] = Field(
        description="NCBI Taxonomy ID to identify the organism",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PySTRENDA.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="46e60bde92f126b86800c25d051b59dd7851ea7d"
    )
