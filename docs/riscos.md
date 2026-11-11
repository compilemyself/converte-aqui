# Análise inicial de riscos

## Segurança e integridade dos arquivos

**Arquivos inválidos ou maliciosos:** podem provocar bugs ou consumo excessivo de recursos. Para reduzir esse risco, serão validados o conteúdo real, o MIME type, a extensão, o tamanho e as dimensões dos arquivos, além da aplicação de limites para uploads.

**Acesso não autorizado a imagens:** a ausência de verificações adequadas pode permitir que usuários acessem arquivos de outras contas. O tratamento previsto consiste em implementar autenticação e verificar a propriedade dos arquivos em todas as operações.

**Exposição de credenciais:** o armazenamento inadequado de credenciais pode comprometer contas e o banco de dados. O arquivo .env já está protegido contra inclusão no Git por meio do .gitignore. Ainda serão implementados o armazenamento de senhas por hash e o uso de HTTPS em ambientes de implantação.

## Persistência e processamento

**Falhas na gravação de arquivos ou registros:** podem gerar inconsistências entre o sistema de arquivos e o PostgreSQL. Serão implementados tratamentos de exceções e mecanismos para coordenar as operações de persistência.

**Perda de arquivos:** falhas de armazenamento ou exclusões acidentais podem comprometer imagens e resultados. Serão implementados tratamentos de erro para essas operações.

## Desenvolvimento e integração

**Diferenças entre ambientes de desenvolvimento:** configurações e dependências distintas entre os computadores dos desenvolvedores podem provocar falhas de execução. A configuração inicial do Docker Compose e o arquivo compartilhado de dependências já foram estabelecidos para facilitar a padronização dos ambientes. As migrações do banco de dados também serão versionadas.