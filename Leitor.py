import xml.etree.ElementTree as et
from pathlib import Path
from os import getcwd

Pathing = getcwd()
p = Path(Pathing)
Xml = list(p.glob('**/livros.xml'))

print(Xml)

for Mob in Xml:

	Arquivo = et.parse(Mob)
	print(Mob)

	ArquivoRoot = Arquivo.getroot()
	print(ArquivoRoot)

	with open(f'{Mob} - Tags', 'w') as f:
		for child in ArquivoRoot.findall('book'):
			autor = child.find('author').text
			titulo = child.find('title').text
			genero = child.find('genre').text
			print(f'Autor: {autor}\nTítulo: {titulo} | Gênero: {genero}\n')

			f.write(f'\nAutor: {autor}\nTítulo: {titulo} | Gênero: {genero}\n')
	f.close

input('-- Fim --')
