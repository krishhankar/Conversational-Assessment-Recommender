from typing import List
from pydantic import BaseModel

class Assessment(BaseModel):
    entity_id: str
    name: str
    link: str
    description: str

    job_levels: List[str]
    languages: List[str]
    duration: str

    remote: str
    adaptive: str

    keys: List[str]

    def embedding_text(self):
        return f"""
        Name:{self.name}
        Description:{self.description}
        Job Levels:{", ".join(self.job_levels)}
        Skills:{", ".join(self.keys)}
        Languages:{", ".join(self.languages)}
        Duration:{self.duration}
        Adaptive:{self.adaptive}
        Remote:{self.remote}   """