from pydantic import BaseModel


class VideoSchema(BaseModel):
    title: str

    class Config:
        from_attributes = True
