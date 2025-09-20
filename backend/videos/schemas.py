from pydantic import BaseModel


class VideoSchema(BaseModel):
    title: str
    duration: int
    path: str
    views_count: int

    class Config:
        from_attributes = True
