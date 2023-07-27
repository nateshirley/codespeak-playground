from pydantic import BaseModel
from typing import List

import codespeak
from codespeak import writable

harmonic_api_key = ""
codespeak.add_api("harmonic", harmonic_api_key)
codespeak.password = ""


class CompanyResponse(BaseModel):
    name: str | None
    website: str | None
    founding_date: str | None
    country: str | None
    highlights: List[str] | None


# you could also have done: typeddict, regular class, list, etc. Whatever you want


@writable
def get_company(company_id: int) -> CompanyResponse:
    pass


response = get_company(company_id=1)
print(response)
