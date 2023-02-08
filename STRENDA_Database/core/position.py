import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .proteinsequence import ProteinSequence


@forge_signature
class Position(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("positionINDEX"),
        xml="@id",
    )
    position_id: Optional[int] = Field(
        description="Equivalent position in the reference sequence",
        default=None,
    )

    protein_sequence_id: Optional[ProteinSequence] = Field(
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
        default=None,
    )

    standard_numbering_scheme_id: Optional[int] = Field(
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
        default=None,
    )

    annotation_id: Optional[int] = Field(
        description=(
            "Function that is found in the annotated amino acid or sub-sequence"
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PySTRENDA.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="46e60bde92f126b86800c25d051b59dd7851ea7d"
    )
