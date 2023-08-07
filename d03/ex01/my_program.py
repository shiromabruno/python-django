from path import Path

def main():

    folder_name = "my_folder"
    file_name = "my_file.txt"

    # criando pasta
    path_obj = Path(folder_name)
    path_obj.mkdir()

    # conteudo do arquivo que ficara dentro da pasta
    file_content = "Testando ex01 no my_program.py"

    # Caminho do arquivo = my_folder/my_file.txt. path_obj = Path("my_folder")
    file_path = path_obj / file_name
    file_path.write_text(file_content)

    # Read the content from the file using Path object
    read_content = file_path.read_text()

    # Display the content
    print("Lendo  arquivo do caminho: ", file_path)
    print(read_content)

    # try:
    #     Path.makedirs('fake_diretory')
    # except FileExistsError as e:
    #     print(e)
    # Path.touch('teste/caminho')
    # f = Path('teste/caminho')
    # f.write_lines(['bruno', 'shiroma', 'mini', 'piscina', '42'])
    # print(f.read_text())


if __name__ == '__main__':
    main()