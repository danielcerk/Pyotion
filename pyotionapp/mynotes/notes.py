from datetime import datetime
import json

data_agora = datetime.now()


class Notes:

	def __init__(self):

		self.nome_note = 'Nota'
		self.nome_antigo = ''
		self.nome_novo = ''
		self.desc = ''
		self.data = data_agora.date()

	#  Precisamos de DATA, DESCRIÇÃO E SABER SE FOI FEITA OU NÃO

	def createNote(self, nome_note, desc):

		if nome_note == '':

			with open('note.json', 'r') as file:

				note = json.load(file)

					
			notes = [{"descricao": desc, 
				"data_criacao": str(self.data)}]

			note[self.nome_note] = notes

			with open('note.json','w') as file:

				json.dump(note, file, indent=4)

				print(f'Nota {self.nome_note} criada')

		else:

			with open('note.json', 'r') as file:

				note = json.load(file)

			if nome_note in note:

				print('Nome já existe . Tente outro')

			else:
					
				notes = [{"descricao": desc, 
				"data_criacao": str(self.data)}]

				note[nome_note] = notes

				with open('note.json','w') as file:

					json.dump(note, file, indent=4)

					print(f'Nota {nome_note} criada')

	def readNote(self, nome_note):

		with open('note.json', 'r') as file:

			note = json.load(file)

		if nome_note in note:

			note_item = note[nome_note]

			for i in note_item:

				desc = i['descricao']
				date_creation = i['data_criacao']
				done = i['feita']

				print(f"Titulo: {nome_note}")
				print(f"Descrição: {desc}")
				print(f"Data de criação: {date_creation}")

		elif nome_note == '' or nome_note == None:

			print('Todas as suas notas')

			for i in note:

				print('-'*10)
				print(f"Titulo: {i}")

				note_item = note[i]
					
				for i in note_item:

					desc = i['descricao']
					date_creation = i['data_criacao']
					done = i['feita']

					print(f"Descrição: {desc}")
					print(f"Data de criação: {date_creation}")


	def updateNote(self, nome_antigo, nome_novo):

		if nome_antigo != '' and nome_novo != '':

			try:

				with open('note.json') as file:

					note = json.load(file)
			
				note[nome_novo] = note[nome_antigo]

				del note[nome_antigo]

				with open('note.json', 'w') as file:

					json.dump(note, file, indent=4)

					print('Nota editada')

			except KeyError:

				print('Não foi possível encontrar sua nota . Verifique se escreveu certo .')

		else:

			print('Não deixe o espaço em branco , se não não é possível deletar a nota .')


	def deleteNote(self, nome_note):

		if nome_note != '':

			try:

				with open('note.json', 'r') as file:

					note = json.load(file)

				del note[nome_note]

				with open('note.json', 'w') as file:

					json.dump(note, file, indent=4)

					print('Item excluido')

			except KeyError:

				print('Não foi possível encontrar sua nota . Verifique se escreveu certo .')

		else:

			print('Não deixe o espaço em branco , se não não é possível deletar a nota .')

