import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .organism import Organism
from .proteindatabase import ProteinDatabase


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )
    protein_sequence_id: Optional[str] = Field(
        description="Presented protein sequence",
        default=None,
    )

    name: Optional[str] = Field(
        description="Systematic name of the protein.",
        default=None,
    )

    amino_acid_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    protein_database_name: Optional[ProteinDatabase] = Field(
        description="Data base ID",
        default=None,
    )

    protein_organism_id: Optional[Organism] = Field(
        description="Corresponding organism",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PySTRENDA.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="46e60bde92f126b86800c25d051b59dd7851ea7d"
    )
