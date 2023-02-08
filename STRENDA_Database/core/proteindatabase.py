import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class ProteinDatabase(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteindatabaseINDEX"),
        xml="@id",
    )
    database: Optional[int] = Field(
        description="Position in the sequence where the domain starts",
        default=None,
    )

    link_to_database: Optional[int] = Field(
        description="Position in the sequence where the domain ends",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PySTRENDA.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="46e60bde92f126b86800c25d051b59dd7851ea7d"
    )
