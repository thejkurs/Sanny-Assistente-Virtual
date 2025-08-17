# 🤖 Sanny - Sua Assistente Virtual em Português

Sanny é uma assistente virtual por voz, desenvolvida em Python, que integra diversas funcionalidades para automatizar tarefas do seu dia a dia. Ela utiliza a API do Google Gemini para interações e responde a comandos de voz para controlar seu computador. A Sanny se encontra na sua versao 1.0 e terá atualizaçoes frequentemente.

---

## ✨ Funcionalidades

Sanny pode realizar uma variedade de tarefas para você. Para interagir com ela, use a palavra de ativação "**Sanny**" ou **algumas pré definidas** (verifique no codigo) seguida do seu comando ou pergunta.

### **Comandos de Voz**

| Categoria | Comando | Exemplo de Uso | Descrição |
| :--- | :--- | :--- | :--- |
| **Geral** | `que horas são?` | Sanny, que horas são? | Informa a hora atual. |
| **Navegação** | `abrir Google` | Sanny, abrir Google | Abre o navegador Google Chrome. |
| **Controle de Apps** | `abrir aplicativo [nome]` | Sanny, abrir aplicativo Discord | Abre um aplicativo específico (veja a seção de configuração). |
| **Spotify** | `abrir Spotify` | Sanny, abrir Spotify | Inicia o aplicativo Spotify. |
| | `tocar playlist Spotify [nome]` | Sanny, tocar playlist Spotify minha playlist de trabalho | Inicia a reprodução de uma playlist específica (veja a seção de configuração). |
| | `listar playlists Spotify` | Sanny, listar playlists Spotify | Informa quais playlists estão configuradas para serem tocadas. |
| **Música Local** | `tocar música [nome]` | Sanny, tocar música Imagine | Toca uma música da sua pasta local `musicas/`. |
| | `parar música` | Sanny, parar música | Pausa a música que está tocando. |
| | `listar músicas` | Sanny, listar músicas | Informa as músicas disponíveis na sua pasta local. |
| **Automação** | `iniciar ambiente de trabalho` | Sanny, iniciar ambiente de trabalho | Executa uma rotina de comandos pré-definida para você (ex: abrir aplicativos de trabalho). |
| **Conversação** | `me responda sobre [pergunta]` | Sanny, me responda sobre a capital do Brasil. | Inicia uma conversa com a IA do Google Gemini. |
| | `continue` | Sanny, continue | Continua a última resposta da IA. |
| **Finalização** | `encerrar` | Sanny, encerrar | Desliga a assistente. |

---

## 🛠️ Como Configurar

Para usar a Sanny, você precisa instalar as dependências e configurar os caminhos e chaves da API.

### **1. Pré-requisitos**

Certifique-se de ter o Python instalado (versão 3.6 ou superior).

### **2. Configurando o Ambiente**

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd nome-do-seu-projeto
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Se você ainda não tem o arquivo `requirements.txt`, execute `pip freeze > requirements.txt` para criá-lo com as dependências atuais).*

### **3. Configuração de Chaves e Caminhos**

Abra o arquivo `config.py` e preencha as informações necessárias:

-   **API do Gemini:**
    ```python
    API_KEY_GEMINI = "SUA_CHAVE_AQUI" 
    ```
    > **Como obter a chave:** Crie uma conta no Google AI Studio e gere uma chave de API para o Gemini.

-   **Caminhos dos Aplicativos (`APPLICATIONS_PATHS`):**
    ```python
    APPLICATIONS_PATHS = {
        "vscode": r"C:\Caminho\Para\O\Seu\VSCode\Code.exe",
        "discord": r"C:\Caminho\Para\O\Seu\Discord\Discord.exe",
    }
    ```
    > **Dica:** Para encontrar o caminho de um aplicativo no Windows, clique com o botão direito no ícone do atalho, vá em "Propriedades" e copie o "Local do destino".

-   **Playlists do Spotify (`PLAYLISTS_SPOTIFY`):**
    ```python
    PLAYLISTS_SPOTIFY = {
        "minha playlist de trabalho": "URL_DA_SUA_PLAYLIST_AQUI",
        "calmante": "URL_DA_SUA_OUTRA_PLAYLIST_AQUI",
    }
    ```
    > **Como obter a URL:** No Spotify, clique com o botão direito na sua playlist, vá em "Compartilhar" e "Copiar Link da Playlist".

-   **Caminho das Músicas (`MUSIC_FOLDER_PATH`):**
    ```python
    MUSIC_FOLDER_PATH = "musicas"
    ```
    > **Dica:** dentro da pasta chamada `musicas` na raiz do projeto, coloque seus arquivos `.mp3` dentro dela.

---

## ▶️ Como Rodar

Após a configuração, basta executar o arquivo principal:

```bash
python main.py
