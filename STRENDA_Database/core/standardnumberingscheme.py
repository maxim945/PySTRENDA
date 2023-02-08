import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .proteinsequence import ProteinSequence


@forge_signature
class StandardNumberingScheme(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("standardnumberingschemeINDEX"),
        xml="@id",
    )

    protein_sequence_id: Optional[ProteinSequence] = Field(
        description="Presented protein sequence", default=None
    )

    standard_numering_scheme_id: Optional[int] = Field(
        description="the id of the scheme", default=None
    )

    standard_numering_scheme_name: Optional[str] = Field(
        description="the name of each standard numbering", default=None
    )

    standard_numering_scheme: Optional[str] = Field(
        description="the numbering scheme for each sequence", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PySTRENDA.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="1c847fc58cf14ea24075c0c271f5f2616aba1ab1"
    )
