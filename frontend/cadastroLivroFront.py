import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def cadastrar_livro():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    editora = campo_editora.get()
    ano = campo_ano.get()
    isbn = campo_isbn.get()

    if titulo and autor and editora and ano and isbn:
        resultado.configure(text="📚 Livro cadastrado com sucesso!", text_color="green")
        # Aqui você pode chamar a função do backend para salvar no banco
        # exemplo: salvar_livro(titulo, autor, editora, ano, isbn)
    else:
        resultado.configure(text="⚠️ Preencha todos os campos!", text_color="yellow")

app = ctk.CTk()
app.title("📘 Cadastro de Livros")
app.geometry("500x550")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=40, padx=40, fill="both", expand=True)

titulo_label = ctk.CTkLabel(frame, text="📘 Cadastro de Livros", font=('Arial', 22, 'bold'))
titulo_label.pack(pady=(20, 10))

campo_titulo = ctk.CTkEntry(frame, placeholder_text="Título do livro")
campo_titulo.pack(padx=20, pady=5, fill="x")

campo_autor = ctk.CTkEntry(frame, placeholder_text="Autor")
campo_autor.pack(padx=20, pady=5, fill="x")

campo_editora = ctk.CTkEntry(frame, placeholder_text="Editora")
campo_editora.pack(padx=20, pady=5, fill="x")

campo_ano = ctk.CTkEntry(frame, placeholder_text="Ano de publicação")
campo_ano.pack(padx=20, pady=5, fill="x")

campo_isbn = ctk.CTkEntry(frame, placeholder_text="ISBN")
campo_isbn.pack(padx=20, pady=5, fill="x")

botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar Livro", command=cadastrar_livro)
botao_cadastrar.pack(pady=15)

resultado = ctk.CTkLabel(frame, text="", font=("Arial", 12, "italic"))
resultado.pack(pady=5)

app.mainloop()