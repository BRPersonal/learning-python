from datetime import datetime,date
from pydantic import BaseModel, Field, computed_field
import json

from custom_json_encoder import CustomJSONEncoder


class NoticeEmailExtract(BaseModel):
    date_of_notice_str: str | None = Field(
        default=None,
        exclude=True,
        repr=False,
        description="""The date of the notice (if any) reformatted
        to match YYYY-mm-dd""",
    )
    entity_name: str | None = Field(
        default=None,
        description="""The name of the entity sending the notice (if present
        in the message)""",
    )

    max_potential_fine: float | None = Field(
        default=None,
        description="""The maximum potential fine
        (if any)""",
    )

    def model_dump(self, **kwargs):
        dump_dict = super().model_dump(**kwargs)
        dump_dict['date_of_notice'] = self.date_of_notice
        return dump_dict

    def model_dump_json(self, **kwargs):
        dump_dict = self.model_dump()
        return json.dumps(dump_dict, cls=CustomJSONEncoder)

    @staticmethod
    def _convert_string_to_date(date_str: str | None) -> date | None:
        if not date_str:
            return None
        else:
            return datetime.strptime(date_str, "%Y-%m-%d").date()

    @computed_field
    @property
    def date_of_notice(self) -> date | None:
        return self._convert_string_to_date(self.date_of_notice_str)

if __name__ == "__main__":

    notice_email_extract = NoticeEmailExtract(
        date_of_notice_str="2024-02-29",
        entity_name="Entity Name",
        max_potential_fine=1000.0,
    )

    #serialize to json string
    notice_str = notice_email_extract.model_dump_json()
    print(f"notice_str: {notice_str}")

    #deserialize from json string
    notice_email_extract_from_json = NoticeEmailExtract.model_validate_json(notice_str)
    print(f"notice_email_extract_from_json: {notice_email_extract_from_json}")

    #check if the two objects are equal
    assert notice_email_extract == notice_email_extract_from_json


