from datetime import date


class Mock:

    @classmethod
    def get_list(cls):
        return [
            {'id': 1, 'name': 'estudar',
             'endDate': date.today(),
             'description': 'Estudar para o TCC'}
            ]
