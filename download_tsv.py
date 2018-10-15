import gzip

import requests


def download_and_unpack_tsv_gz(url: str, filename: str):
    with open(f'{filename}.tsv.gz', 'wb') as gz_file:
        gz_content = requests.get(url)
        gz_file.write(gz_content.content)

    with gzip.open(f'{filename}.tsv.gz') as gz_file:
        data = gz_file.read()
        with open(f'{filename}.tsv', 'wb') as tsv_file:
            tsv_file.write(data)


if __name__ == '__main__':
    download_and_unpack_tsv_gz(
        'https://datasets.imdbws.com/name.basics.tsv.gz', 'name.basics')
    download_and_unpack_tsv_gz(
        'https://datasets.imdbws.com/title.basics.tsv.gz', 'title.basics')
