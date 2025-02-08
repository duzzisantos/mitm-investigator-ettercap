from fastapi import APIRouter
from pydantic import BaseModel
from api.RunEttercap import run_ettercap

ettercap_process = APIRouter()


class NetworkInterface(BaseModel):
    interface: str


@ettercap_process.post("/GetEtterCapInvestigation")
def use_ettercap(item: NetworkInterface):
    return run_ettercap(item.interface)
