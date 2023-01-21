import requests


def generate_dict(id, directors, genre, year, name):
    return {
    'id': id, 
    'directors': directors, 
    'genre': genre, 
    'year': year, 
    'name': name
}


requests.post('http://127.0.0.1:5000/books', json=generate_dict(
    1, ['Kentaro_Miura'], genre='black_fantasy', year=1989, name='Berserk'
    ))
requests.post('http://127.0.0.1:5000/books', json=generate_dict(
    2, ['Antoine_de_Saint-Exupery'], genre='philosophical_tale', year=1942, name='Le_Petit_Prince'
))
requests.patch('http://127.0.0.1:5000/books', json={
    'id': 2,
    'genre': 'philosophical_tale'
})
requests.delete('http://127.0.0.1:5000/books/1')
