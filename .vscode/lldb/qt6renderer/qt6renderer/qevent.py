from lldb import SBValue, eBasicTypeLongLong, eBasicTypeUnsignedShort
from .abstractsynth import AbstractSynth
from .syntheticstruct import SyntheticStruct


class QEventSynth(AbstractSynth):
    def get_child_index(self, name: str) -> int:
        if name == QEventSyntheticStruct.PROP_TYPE:
            return 0
        else:
            return -1

    def update(self) -> bool:
        event = QEventSyntheticStruct(self._valobj)
        self._values = [event.type()]
        self._values.extend(self._valobj.children)
        return False


class QEventSyntheticStruct(SyntheticStruct):
    PROP_TYPE = 'type'

    def __init__(self, pointer: SBValue):
        super().__init__(pointer)
        self.add_basic_type_field('unknown', eBasicTypeLongLong)

        t_event_type = pointer.target.FindFirstType('QEvent::Type')
        if t_event_type.IsValid():
            self.add_sb_type_field(QEventSyntheticStruct.PROP_TYPE, t_event_type)
        else:
            self.add_basic_type_field(QEventSyntheticStruct.PROP_TYPE, eBasicTypeUnsignedShort)

    def unknown(self) -> SBValue:
        pass

    def type(self) -> SBValue:
        pass
