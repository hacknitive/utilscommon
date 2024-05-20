from typing import Optional

from pydantic import BaseModel


class SchemaBoto3(BaseModel):
    HOST: str
    PORT: int
    SERVER_ACCESS_KEY: str
    SERVER_SECRET_KEY: str
    SERVER_ADDRESS_FOR_CLIENT: str
    SCHEDULER_INTERVAL_FOR_DELETE_USELESS_OBJECTS_IN_DAYS: Optional[int] = None
    EXPIRATION_DURATION_FOR_TEMPORARY_URLS_IN_HOURS: Optional[int] = None
