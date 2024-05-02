from typing import Literal, Optional

import boto3
import botocore
from pydantic import BaseModel
from datetime import datetime


class StreamSchema(BaseModel):

    title: str
    stream_name: str
    file_url: str
    stream_id: int
    # schedule: Optional[datetime]
    # action: Optional[Literal["START", "STOP", "SCHEDULE"]]
