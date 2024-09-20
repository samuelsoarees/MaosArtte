import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('itens.db')
cursor = conn.cursor()

# Criar tabela de itens
def criar_tabela():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            quantidade NUMBER
        )
    ''')
    conn.commit()

# Criar item
def criar_item(nome, descricao):
    cursor.execute('''
        INSERT INTO item (nome, descricao) VALUES (?, ?)
    ''', (nome, descricao))
    conn.commit()

# Ler itens
def ler_itens():
    cursor.execute('SELECT * FROM item')
    return cursor.fetchall()

# Atualizar item
def atualizar_item(item_id, novo_nome, nova_descricao):
    cursor.execute('''
        UPDATE item
        SET nome = ?, descricao = ?
        WHERE id = ?
    ''', (novo_nome, nova_descricao, item_id))
    conn.commit()

# Deletar item
def deletar_item(item_id):
    cursor.execute('DELETE FROM item WHERE id = ?', (item_id,))
    conn.commit()

# Adicionar Quantidade
def adicionar_Quantidade(item_id, qtde):
    cursor.execute('UPDATE ITEM SET QUANTIDADE = QUANTIDADE + ? WHERE ITEM.ID = ?', (qtde, item_id))
    conn.commit()

# Função principal
def main():
    criar_tabela()
    
    while True:
        print("\nMenu:")
        print("1. Criar item")
        print("2. Ler itens")
        print("3. Atualizar item")
        print("4. Deletar item")
        print("5. Adicionar quantidade item")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do item: ")
            descricao = input("Digite a descrição do item: ")
            criar_item(nome, descricao)
            print("Item criado com sucesso!")

        elif escolha == '2':
            itens = ler_itens()
            print("\nItens:")
            for item in itens:
                print(f"ID: {item[0]}, Nome: {item[1]}, Descrição: {item[2]}")

        elif escolha == '3':
            item_id = int(input("Digite o ID do item a ser atualizado: "))
            novo_nome = input("Digite o novo nome do item: ")
            nova_descricao = input("Digite a nova descrição do item: ")
            atualizar_item(item_id, novo_nome, nova_descricao)
            print("Item atualizado com sucesso!")

        elif escolha == '4':
            item_id = int(input("Digite o ID do item a ser deletado: "))
            deletar_item(item_id)
            print("Item deletado com sucesso!")

        elif escolha == '5':
            item_id = int(input("Digite o ID do item a ser incrementado: "))
            quantidade = int(input("Digite a quantidade do item: "))
            adicionar_Quantidade(item_id, quantidade)
            print("Item deletado com sucesso!")        

        elif escolha == '6':
            break

        else:
            print("Opção inválida!")

# Executar o programa
if __name__ == "__main__":
    main()

# Fechar a conexão ao final
conn.close()