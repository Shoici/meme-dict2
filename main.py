meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
comm = input('Masukkan command : ')

if comm in meme_dict.keys():
    print(meme_dict[comm])
else:
    print('Maaf kata tersebut belum ditambahkan ke dalam kamus kami')
