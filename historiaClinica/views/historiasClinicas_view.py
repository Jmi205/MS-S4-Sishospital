from fastapi import APIRouter, status, Body
import logic.historiasClinicas_logic as historiasClincas_service
from models.models import HistoriaClinica, HistoriaClinicaOut, HistoriaClinicaCollection

router = APIRouter()
ENDPOINT_NAME = "/historiasClinicas"


@router.get(
    "/",
    response_description="List all Historias Clinicas",
    response_model=HistoriaClinicaCollection,
    status_code=status.HTTP_200_OK,
)
async def get_historiasClinicas():
    return await historiasClincas_service.get_historiasClinicas()


@router.get(
    "/{historiaClinica_code}",
    response_description="Get a single HIstoria Clinica by its code",
    response_model=HistoriaClinicaOut,
    status_code=status.HTTP_200_OK,
)
async def get_historiaClinica(historiaClinica_code: str):
    return await historiasClincas_service.get_historiaClinica(historiaClinica_code)


@router.post(
    "/",
    response_description="Create a new historiaClinica",
    response_model= HistoriaClinicaOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_historiaClinica(historiaClinica: HistoriaClinica = Body(...)):
    return await historiasClincas_service.create_historiaClinica(historiaClinica)


@router.put(
    "/{historiaClinica_code}",
    response_description="Update a historiaClinica",
    response_model=HistoriaClinicaOut,
    status_code=status.HTTP_200_OK,
)
async def update_historiaClinica(historiaClinica_code: str, historiaClinica: HistoriaClinica = Body(...)):
    return await historiasClincas_service.update_historiaClinica(historiaClinica_code, historiaClinica)


@router.delete(
    "/{historiaClinica_code}",
    response_description="Delete a HistoriaClinica",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_historiaClinica(historiaClinica_code: str):
    return await historiasClincas_service.delete_historiaClinica(historiaClinica_code)
