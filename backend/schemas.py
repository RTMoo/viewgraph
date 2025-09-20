from pydantic import BaseModel


class VideoSchema(BaseModel):
    title: str
    duration: int
    path: str

    class Config:
        from_attributes = True
