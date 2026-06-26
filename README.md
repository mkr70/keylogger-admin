# Monitor de Teclado com Envio Automatizado (Keylogger Educacional)

Este projeto consiste em uma ferramenta em Python desenvolvida para monitorar entradas de teclado (keylogger), registrar as informações em um arquivo local e encaminhar os logs periodicamente para um endereço de e-mail configurado através do protocolo SMTP.

> **Aviso Importante:** Este projeto possui fins estritamente educacionais e de demonstração técnica de segurança da informação. O autor não se responsabiliza pelo uso indevido deste software.

## 🚀 Recursos

* **Verificação de Privilégios**: Detecta automaticamente se está rodando como Administrador no Windows.
* **Auto-Elevação**: Solicita permissões de administrador automaticamente caso necessário (UAC).
* **Captura Inteligente**: Distingue caracteres alfanuméricos de teclas especiais (como Espaço, Enter e Esc).
* **Buffer Local**: Grava e envia os dados a cada 50 toques de tecla para evitar perda de dados.
* **Envio por E-mail**: Anexa o arquivo `log.txt` e o envia via SMTP_SSL (configurado para o Gmail).

## 📋 Pré-requisitos

O script utiliza bibliotecas nativas do Python e a biblioteca externa `pynput` para captura de eventos de hardware.

### Instalação das Dependências

Instale a biblioteca necessária através do gerenciador de pacotes pip:

```bash
pip install pynput
```

## ⚙️ Configuração

Antes de executar, você precisa configurar as credenciais de envio de e-mail diretamente no código-fonte. Abra o arquivo do script e modifique as variáveis abaixo:

1. Defina as variáveis de configuração iniciais:
   ```python
   REMETENTE = "seu-email@gmail.com"
   SENHA_APP = "sua-senha-de-app-de-16-digitos"
   DESTINO = "email-destino@gmail.com"
   ```

2. Atualize também os campos vazios dentro da função `enviar_email()`:
   ```python
   msg["From"] = "seu-email@gmail.com"
   msg["To"] = "email-destino@gmail.com"
   
   # ... dentro do bloco try:
   smtp.login("seu-email@gmail.com", "sua-senha-de-app-de-16-digitos")
   ```

> **Dica**: Para utilizar o Gmail, você precisa gerar uma **Senha de App** de 16 dígitos nas configurações de segurança da sua Conta Google. Senhas comuns de login não funcionarão devido às proteções contra aplicativos menos seguros.

## 💻 Como Executar

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta do arquivo.
3. Execute o comando:

```bash
python nome_do_seu_arquivo.py
```

*Nota: Uma janela de permissão de Administrador do Windows (UAC) será aberta para validar a execução com privilégios elevados.*

## 🛑 Como Encerrar

Para parar a execução do script e interromper o monitoramento do teclado, basta pressionar a tecla `ESC` no seu teclado.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **pynput** (Monitoramento de periféricos)
* **ctypes** (Interação com a API de sistema do Windows)
* **smtplib & email** (Gerenciamento e envio de e-mails de forma nativa)
