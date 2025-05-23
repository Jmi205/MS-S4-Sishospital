import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://sishospital_user:isis2503@10.128.0.86:27017?retryWrites=true&w=majority"
)
db = client.get_database("sishopital_db")
historiasClinicas_collection = db.get_collection("historiasClinicas")


async def set_historiasClinicas_db():
    # Creates a unique index on the code field
    await historiasClinicas_collection.create_index("code", unique=True)


# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]
