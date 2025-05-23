# Models for the places microservice

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId



class HistoriaClinica(BaseModel):
    date: str = Field(...)
    observations: str = Field(...)
    lastupdate: str = Field(...)
    code: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "dateCreation": "27/08/2005",
                "observations": "El paciente tiene un morado en la pierna por un golpe.",
                "lastupdate" :  "27/08/2025",
                "code" : "HU8585"
            }
        },
    )


class HistoriaClinicaOut(HistoriaClinica):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "64b9f1f4f1d2b2a3c4e5f6a7",
                "date": "27/08/2005",
                "observations": "El paciene tiene un morado en la pierna por un golpe.",
                "lastUpdate" :  "27/08/2025",
                "code" : "HU8585"
            }
        },
    )


class HistoriaClinicaCollection(BaseModel):
    # A collection of places
    historiasClinicas: List[HistoriaClinicaOut] = Field(...)
