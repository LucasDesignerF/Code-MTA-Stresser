# Code Stresser Test - MTA San Andreas

O **Code Stresser Test** é uma ferramenta desenvolvida para testar a resistência de servidores do **MTA San Andreas** contra diferentes tipos de ataques de negação de serviço (DDoS). Este projeto permite que você configure ataques simulados para testar a capacidade do seu servidor em lidar com tráfego excessivo.

## Funcionalidades

- **SYN Flood**: Ataque que explora a forma como o protocolo TCP funciona, enviando pacotes com o flag SYN ativado e causando uma sobrecarga no servidor.
- **UDP Flood**: Envio massivo de pacotes UDP para o servidor, com o objetivo de esgotar os recursos de rede.
- **Sobrecarga de HTTP**: Envio de requisições HTTP em grande volume para sobrecarregar a capacidade do servidor.
- **Fragmentação de Pacotes**: Fragmentação de pacotes para tentar burlar as verificações de pacotes no servidor.

## Tecnologias Usadas

- **HTML** e **CSS** para a interface do usuário.
- **Bootstrap 5** para responsividade e estilo.
- **JavaScript** para a lógica do lado do cliente e interação com a API.
- **Flask** para a parte de backend que gerencia os ataques.
- **JSON** para a comunicação entre o cliente e o servidor.

## Como Usar

### Requisitos

- Um servidor com **Python 3.x** e **Flask** instalado.
- O acesso a um servidor MTA San Andreas para realizar os testes de estresse.

### Passos para Configuração

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/LucasDesignerF/Code-MTA-Stresser.git
    cd code-stresser-mta
    ```

2. **Instale as dependências**:

    Instale as bibliotecas necessárias para rodar o backend:

    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o servidor Flask**:

    Execute o servidor para testar os ataques:

    ```bash
    python stresser.py
    ```

4. **Acesse a interface**:

    Abra o navegador e vá até `http://localhost:5000` para acessar a interface web do stresser.

5. **Configure o Ataque**:

    - Insira o **IP de Destino** do servidor MTA San Andreas.
    - Defina a **porta** do servidor.
    - Escolha o **tipo de ataque** que deseja realizar.
    - Configure o **número de threads** e a **duração** do ataque.

6. **Inicie o Ataque**:

    Clique no botão "Iniciar Ataque" e o stresser começará a enviar os pacotes para o servidor alvo.

## Estrutura de Diretórios

```
/code-stresser-mta
├── stresser.py               # Backend em Flask para gerenciar ataques
├── stresser.html             # Frontend em HTML, Bootstrap5, CSS e JavaScript
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork, abrir issues ou enviar pull requests.

### Como Contribuir

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Comite suas alterações (`git commit -am 'Adicionando nova feature'`).
4. Faça o push da sua branch (`git push origin feature/nova-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a **MIT License** - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Aviso

Este stresser foi projetado apenas para **testes e simulações** em ambientes controlados. O uso indevido de ferramentas de estresse e ataques DDoS em servidores sem permissão é ilegal e pode resultar em consequências legais. Use com responsabilidade.

---

**Code Stresser Test - MTA San Andreas**  
Desenvolvido com 💻 por **[LucasDev]**  
2025 - Todos os direitos reservados
```

### O que está incluído no README:

1. **Introdução** ao projeto, explicando o propósito e os tipos de ataques.
2. **Tecnologias usadas** para dar uma visão geral do que foi utilizado no desenvolvimento.
3. **Passos para uso** do stresser, desde o clone do repositório até a execução.
4. **Estrutura de diretórios** para mostrar como os arquivos estão organizados.
5. **Instruções para contribuir** com o projeto, caso alguém queira ajudar.
6. **Aviso legal** sobre o uso responsável da ferramenta.

Esse README deve fornecer as informações necessárias para qualquer usuário ou colaborador interessado no projeto.