# Contrato inicial da API REST

Prefixo planejado: `/api/v1`. JSON será o formato principal.

## Rotas existentes

| Método | Rota | Estado |
|---|---|---|
| GET | `/` | Implementada: informações básicas da API |
| GET | `/api/v1/health` | Implementada: verifica se a API responde; não verifica o banco |


## Rotas planejadas

### Autenticação e conta
| Método | Rota | Finalidade |
|---|---|---|
| POST | `/api/v1/auth/register` | Criar conta |
| POST | `/api/v1/auth/login` | Autenticar e obter credencial de acesso |
| GET | `/api/v1/users/me` | Consultar conta autenticada |
| PUT | `/api/v1/users/me` | Atualizar dados da conta |
### Imagens

| Método | Rota | Finalidade |
|---|---|---|
| POST | `/api/v1/images` | Enviar e cadastrar imagem (`multipart/form-data`) |
| GET | `/api/v1/images` | Listar imagens da conta autenticada |
| GET | `/api/v1/images/{image_id}` | Consultar imagem |
| PUT | `/api/v1/images/{image_id}` | Atualizar metadados editáveis |
| DELETE | `/api/v1/images/{image_id}` | Excluir imagem e conversões associadas |

### Conversões e histórico
| Método | Rota | Finalidade |
|---|---|---|
| POST | `/api/v1/images/{image_id}/conversions` | Criar conversão/compressão/redimensionamento |
| GET | `/api/v1/conversions` | Listar histórico da conta autenticada |
| GET | `/api/v1/conversions/{conversion_id}` | Consultar detalhes da conversão |

## Exemplo de parâmetros de conversão

```json
{
  "output_format": "webp",
  "quality": 75,
  "width": 1920,
  "height": 1080,
  "resize_mode": "contain"
}
```

Os valores são uma proposta inicial e serão validados nos schemas da API.