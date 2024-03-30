import pydantic
from typing import List


class MyModel(pydantic.BaseModel):
    class Config:
        extra = "allow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for field_name in kwargs:
            if field_name not in self.__fields__:
                print(f"Extra field \"{field_name}\" found in \"{self.__class__.__name__}\" during validation.")


class HeadingFirst(MyModel):
    company: str
    project: str | int


class HeadingSecond(MyModel):
    number: str | int


class BodyFirst(MyModel):
    company_name: str
    company_address: str
    court_name: str
    date_from: str
    case_number: str | int
    financial_organization: str
    ogrn: str | int
    iin: str | int
    reg_address: str


class TableRow(MyModel):
    pp_number: str | int
    lot_number: str | int
    pp_date: str
    winner_name: str
    payment_purpose: str
    payment_sum: str


class BodySecond(MyModel):
    tbl_contents: List[TableRow]
    total_amount: str


class BottomFirst(MyModel):
    sign: str
    day: str | int
    month: str | int
    year: str | int


class BottomSecond(MyModel):
    full_name: str
    credentials: str


ordering = {
    "heading_1.docx": HeadingFirst,
    "heading_2.docx": HeadingSecond,
    "body_1.docx": BodyFirst,
    "body_2.docx": BodySecond,
    "bottom_1.docx": BottomFirst,
    "bottom_2.docx": BottomSecond,
}
