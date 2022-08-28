from pydantic import BaseModel


class Bank(BaseModel):
    ifsc_first4: str
    is_enach_net_active: bool
    is_enach_card_active: bool
    is_enach_esign_active: bool
    is_active: bool
