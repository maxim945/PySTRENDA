import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .proteinsequence import ProteinSequence


@forge_signature
class StandardNumberingScheme(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("standardnumberingschemeINDEX"),
        xml="@id",
    )
    protein_sequence_id: Optional[ProteinSequence] = Field(
        description="Presented protein sequence",
        default=None,
    )

    standard_numering_scheme_id: Optional[int] = Field(
        description="the id of the scheme",
        default=None,
    )

    standard_numering_scheme_name: Optional[str] = Field(
        description="the name of each standard numbering",
        default=None,
    )

    standard_numering_scheme: Optional[str] = Field(
        description="the numbering scheme for each sequence",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PySTRENDA.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="46e60bde92f126b86800c25d051b59dd7851ea7d"
    )
