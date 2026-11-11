# Modelo inicial de dados

O banco relacional será PostgreSQL. Os arquivos de imagem ficarão no armazenamento do servidor; o banco guardará metadados, caminhos e relacionamentos.

## Entidades previstas

### users

- `id`: chave primária.
- `name`: nome de exibição.
- `email`: e-mail único.
- `password_hash`: hash seguro da senha (provavelmente usando bcrypt); nunca armazenar senha em texto puro.
- `created_at`: data de criação.

### images

- `id`: chave primária.
- `user_id`: chave estrangeira para `users`.
- `original_filename`: nome original enviado.
- `storage_path`: caminho do arquivo original.
- `mime_type` e `format`: tipo/formato identificado.
- `size_bytes`: tamanho original.
- `width` e `height`: dimensões originais em pixels.
- `uploaded_at`: data do envio.

### conversions

- `id`: chave primária.
- `image_id`: chave estrangeira para `images`.
- `output_path`: caminho do resultado.
- `output_format`: JPEG, PNG ou WebP.
- `quality`: parâmetro de qualidade, quando aplicável.
- `target_width` e `target_height`: dimensões solicitadas.
- `resize_mode`: estratégia de ajuste de proporção, quando aplicável.
- `output_size_bytes`: tamanho resultante.
- `created_at`: data da conversão.

## Relacionamentos

- Um usuário possui várias imagens (1:N).
- Uma imagem pode possuir várias conversões (1:N).

As operações devem verificar se a imagem pertence ao usuário autenticado. Exclusões devem tratar os registros e os arquivos associados.
Este é um modelo conceitual inicial; tabelas e migrações ainda serão implementadas.