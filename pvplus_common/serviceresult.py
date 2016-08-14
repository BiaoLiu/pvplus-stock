# coding:utf-8


# service_result = {'data': '', 'ruleviolations': []}
#
# rule_violation = {'parametername': '', 'errormessage': ''}


class ServiceResult:
    def __init__(self):
        self._data = ''
        self._ruleviolations = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def ruleviolations(self):
        return self._ruleviolations


class RuleViolation:
    def __init__(self, parametername, errormessage):
        self.parametername = parametername
        self.errormessage = errormessage


def is_empty(value):
    return len(value) == 0
