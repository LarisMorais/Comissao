

# 📊📱 Envio de SMS para Vendedores com Comissões

Este projeto em Python automatiza o processo de notificação de vendedores que atingiram um valor de vendas mensal superior a R$55.000,00. O script lê arquivos Excel com os dados de vendas, identifica os vendedores que ultrapassaram esse valor e envia uma mensagem SMS personalizada utilizando a API da Twilio.

## 🔍 Sobre o Projeto

O objetivo deste projeto é:

1. **Analisar arquivos Excel**: Ler dados de vendas mensais de diferentes arquivos Excel.
2. **Identificar vendedores elegíveis**: Verificar se algum vendedor atingiu vendas superiores a R$55.000,00.
3. **Enviar notificações via SMS**: Utilizar a API da Twilio para enviar mensagens SMS aos vendedores que atingiram a meta.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Bibliotecas:
  - `pandas`
  - `openpyxl`
  - `twilio`

## 📁 Estrutura do Projeto

- `main.py`: Script principal que executa todas as etapas do projeto.
- Arquivos Excel (`janeiro.xlsx`, `fevereiro.xlsx`, etc.): Contêm os dados de vendas mensais.

## 🚀 Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.
- Conta na Twilio com as credenciais de SID e Token.
- Arquivos Excel com os dados de vendas no mesmo diretório do script.

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/LarisMorais/Comissao.git
   cd Comissao
   ```

2. Instale as dependências:

   ```bash
   pip install pandas openpyxl twilio
   ```

3. Configure suas credenciais da Twilio no script `main.py`:

   ```python
   account_sid = 'SEU_ACCOUNT_SID'
   auth_token = 'SEU_AUTH_TOKEN'
   ```

4. Execute o script:

   ```bash
   python main.py
   ```

   O script analisará os arquivos Excel e enviará SMS para os vendedores que atingiram a meta.

## 📬 Contato

Se desejar entrar em contato, você pode me encontrar em:

 [LinkedIn](https://www.linkedin.com/in/larissamorais26/)
- [GitHub](https://github.com/LarisMorais)
- Email: larismorais26@gmail.com
