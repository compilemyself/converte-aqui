
# Arquitetura inicial

## Camadas e padrão arquitetural

A aplicação será organizada em três camadas principais, utilizando o padrão arquitetural MVC (Model–View–Controller) como referência para a separação de responsabilidades.

1. **Apresentação (View):** cliente web desenvolvido em PHP, HTML, CSS e JavaScript, responsável pela interface e interação com o usuário. O PHP consome a API por HTTP; o cliente não acessa diretamente o PostgreSQL.

2. **Controle (Controller):** endpoints da API REST desenvolvida em FastAPI, responsáveis por receber requisições, validar parâmetros, controlar o fluxo das operações e encaminhar as solicitações aos serviços correspondentes.

3. **Modelo e serviços (Model):** componentes responsáveis pela representação dos dados, acesso ao PostgreSQL e execução das regras de negócio. Inclui também os serviços de processamento de imagens com Pillow.

A persistência será realizada no PostgreSQL, enquanto os arquivos originais e convertidos serão armazenados no sistema de arquivos.

## Fluxo esperado de conversão

1. O usuário autentica-se no cliente web.
2. Envia uma imagem e seleciona formato, qualidade e dimensões.
3. A View encaminha a requisição à API REST.
4. O Controller recebe a solicitação e valida a propriedade do arquivo e os parâmetros.
5. Os serviços de aplicação executam as regras de negócio e utilizam Pillow para produzir o arquivo resultante.
6. O arquivo é salvo no armazenamento e os metadados são registrados no PostgreSQL.
7. A API retorna os dados da conversão em JSON.
8. A View apresenta a comparação e disponibiliza o resultado ao usuário.

## Estado no primeiro commit

Somente a aplicação FastAPI mínima e a página PHP inicial estão implementadas. Conexão com o banco, autenticação, endpoints de recursos e processamento serão adicionados em etapas posteriores.