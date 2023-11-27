"""Transport zone module."""
from dataclasses import dataclass


@dataclass
class TransportZone:
    """Class TransportZone."""
    id: int
    remark: str

    def get_id(self) -> int:
        """Return id."""
        return self.id

    def get_remark(self) -> str:
        """Return remark."""
        return self.remark
