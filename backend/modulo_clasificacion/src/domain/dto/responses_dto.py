from dataclasses import dataclass
from typing import List, Dict


@dataclass

class ResponseDTO():
    
    status_code: int
    success: bool
    message: str
    data: List[Dict]


