
from collections import namedtuple

from src.settings.settings import DATABASE_INFORMATION_FIELDS


class WorkTimeInformationTuple(namedtuple(typename="WorkTimeTuple",
                                          field_names=DATABASE_INFORMATION_FIELDS)):

    def __repr__(self) -> str:
        return f"{self.year}-{self.month}-{self.day} | {int(self.hours):02.0f}:{int(self.minutes):02.0f}:{int(self.seconds):02.0f}"

