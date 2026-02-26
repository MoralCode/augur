from dataclasses import dataclass
from .util import AugurPlatformType
from datetime import datetime

@dataclass
class AugurForgeUser:
    """Data class to act as an adapter layer between augur
    and different platforms representations of a user"""
    
    identifier: int
    username: str
    name: str
    company: str
    location: str
    email: str
    user_type: str
    is_admin: bool
    created_at: datetime
    updated_at: datetime
    source_forge_type: AugurPlatformType # heh sourceforge
    source_forge_domain: str
