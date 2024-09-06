from pydantic import BaseModel


class ClassificationResponse(BaseModel):
    healthy_pallet: bool
