import json
import tkinter as tk
from tkinter import messagebox, filedialog

def processar_json():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo JSON",
        filetypes=[("Arquivos JSON", "*.json")]
    )

    if not caminho_arquivo:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
        return

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            data = json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        messagebox.showerror("Erro", "Erro ao processar o arquivo JSON.")
        return

    faturamentos = [item["valor"] for item in data if item.get("valor", 0) > 0]

    if not faturamentos:
        messagebox.showinfo("Resultado", "Nenhum faturamento válido encontrado.")
        return
    menor = min(faturamentos)
    maior = max(faturamentos)
    soma = sum(faturamentos)
    media = soma / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media)

    resultado = (
        f"Menor valor de faturamento: {menor}\n"
        f"Maior valor de faturamento: {maior}\n"
        f"Número de dias com faturamento acima da média: {dias_acima_da_media}"
    )
    messagebox.showinfo("Resultado", resultado)

janela = tk.Tk()
janela.title("Análise de Faturamento")

tk.Label(janela, text="Clique no botão para importar um arquivo JSON:").pack(pady=5)
tk.Button(janela, text="Importar JSON", command=processar_json).pack(pady=10)

janela.mainloop()
