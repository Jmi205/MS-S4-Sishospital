"""
This module contains the logic for the places app.
Main functions:
- get_places: Get a list of all places
- get_place: Get a single place
- create_place: Create a new place
- update_place: Update a place
- delete_place: Delete a place
"""

from models.models import HistoriaClinica, HistoriaClinicaCollection
from models.db import historiasClinicas_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException


async def get_historiasClinicas():
    """
    Get a list of historias clinicas
    :return: A list of historias clinicas
    """
    historiasClinicas = await historiasClinicas_collection.find().to_list(1000)
    return HistoriaClinicaCollection(historiasClinicas=historiasClinicas)


async def get_historiaClinica(historiaClinica_code: str):
    """
    Get a single historiaClinica
    :param historiaClinica_code: The code of the historiaClinica
    :return: The historiaClinica
    """
    if (historiaClinica := await historiasClinicas_collection.find_one({"code": historiaClinica_code})) is not None:
        return historiaClinica

    raise HTTPException(
        status_code=404, detail=f"HistoriaClinica with code {historiaClinica_code} not found"
    )


async def create_historiaClinica(historiaClinica: HistoriaClinica):
    """
    Insert a new historiaClinica record.
    """

    try:
        new_historiaClinica = await historiasClinicas_collection.insert_one(
            historiaClinica.model_dump(by_alias=True, exclude=["id"])
        )
        created_historiaClinica = await historiasClinicas_collection.find_one({"_id": new_historiaClinica.inserted_id})
        return created_historiaClinica

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"HistoriaClinica with code {historiaClinica.id} already exists"
        )


async def update_historiaClinica(historiaClinica_code: str, historiaClinica: HistoriaClinica):
    """
    Update a Historia Clinica
    :param historiaClinica_code: The code of the Historia Clinica
    :param historiaClinica: The historiaClinica data
    :return: The updated Historia Clinica
    """

    try:
        update_result = await historiasClinicas_collection.update_one(
            {"code": historiaClinica_code},
            {"$set": historiaClinica.model_dump(by_alias=True, exclude=["id"])},
        )
        if update_result.modified_count == 1:
            if (
                updated_historiaClinica := await historiasClinicas_collection.find_one({"code": historiaClinica.code})
            ) is not None:
                return updated_historiaClinica
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"Historia Clinica with code {historiaClinica.code} already exists"
        )

    raise HTTPException(
        status_code=404,
        detail=f"Historia Clinica with code {historiaClinica_code} not found or no updates were made",
    )


async def delete_historiaClinica(historiaClinica_code: str):
    """
    Delete a historiaClinica
    :param place_code: The code of the historiaCLinica
    """
    delete_result = await historiasClinicas_collection.delete_one({"code": historiaClinica_code})

    if delete_result.deleted_count == 1:
        return

    raise HTTPException(
        status_code=404, detail=f"Place with code {historiaClinica_code} not found"
    )
