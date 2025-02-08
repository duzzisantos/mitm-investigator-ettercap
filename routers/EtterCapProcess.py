from fastapi import APIRouter
from api.RunEttercap import run_ettercap

ettercap_process = APIRouter()


@ettercap_process.post("/GetEtterCapInvestigation")
def use_ettercap():
    return run_ettercap("en0")
