class PesertaSeminar:
    def __init__(self):
        self.nama = 'unnamed'
        self.usia = 20
        self.alamat = 'jogja'

    def __repr__(self):

        return 'Nama {}, usia {}, alamat {}'.format(self.nama, self.usia, self.alamat)

