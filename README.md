# Na Hora Certa

Ferramenta de aluguel de sala comercial desenvolvida em Python com o framework Flask.

---

## Requisitos

- Python 3.8+
- SQLite

---

## Instalação

1. Navegue até o diretório do projeto:
   ```bash
   cd {caminho}/na-hora-certa
   ```

2. Instale as dependências:
   ```bash
   pip install -r ./api/requirements.txt
   ```

---

## Execução

```bash
python api/app.py
```

A API estará disponível em `http://localhost:5000`.

A documentação interativa (Swagger) pode ser acessada em:
- `http://localhost:5000/swagger`
- `http://127.0.0.1:5000/swagger`

---

## Endpoints

### `POST /create-new-room`
Cria uma nova sala no banco de dados.

**Body (JSON):**
| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `zip_code` | string | Sim | CEP da sala |
| `address` | string | Sim | Endereço da sala |
| `size` | integer | Sim | Tamanho em m² |
| `documents_ok` | boolean | Sim | Documentação em ordem |
| `condominium_fee` | number | Sim | Taxa de condomínio |
| `iptu` | number | Sim | Valor do IPTU |
| `number_of_bathrooms` | integer | Sim | Número de banheiros |
| `has_parking_space` | boolean | Sim | Possui vaga de estacionamento |
| `has_reception` | boolean | Sim | Possui recepção |
| `doctors_office` | boolean | Sim | Elegível para consultório médico |

**Respostas:**
- `200 OK` — Sala criada com sucesso. Retorna o `room_id` gerado.
- `500 Internal Server Error` — Falha ao criar a sala.

---

### `PUT /update-room/<room_id>`
Atualiza os dados de uma sala existente. Apenas os campos enviados no body serão atualizados.

**Parâmetro de rota:**
| Parâmetro | Tipo | Descrição |
|---|---|---|
| `room_id` | integer | ID da sala a ser atualizada |

**Body (JSON) — todos os campos são opcionais:**
| Campo | Tipo | Descrição |
|---|---|---|
| `zip_code` | string | CEP da sala |
| `address` | string | Endereço da sala |
| `size` | integer | Tamanho em m² |
| `documents_ok` | boolean | Documentação em ordem |
| `condominium_fee` | number | Taxa de condomínio |
| `iptu` | number | Valor do IPTU |
| `number_of_bathrooms` | integer | Número de banheiros |
| `has_parking_space` | boolean | Possui vaga de estacionamento |
| `has_reception` | boolean | Possui recepção |
| `doctors_office` | boolean | Elegível para consultório médico |

**Respostas:**
- `200 OK` — Sala atualizada com sucesso. Retorna o `room_id`.
- `400 Bad Request` — Body da requisição não é JSON.
- `404 Not Found` — Sala não encontrada.

---

### `DELETE /delete-room`
Deleta uma sala existente no banco de dados.

**Body (JSON):**
| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id` | integer | Sim | ID da sala a ser deletada |

**Respostas:**
- `200 OK` — Sala deletada com sucesso.
- `500 Internal Server Error` — Falha ao deletar a sala.

---

### `GET /get-last-10-rooms`
Retorna os últimos 10 registros de salas cadastradas, ordenados pelo ID decrescente.

**Respostas:**
- `200 OK` — Lista com até 10 salas.

---

## Estrutura do Projeto

```
na-hora-certa/
└── api/
    ├── app.py               # Definição das rotas Flask
    ├── requirements.txt     # Dependências do projeto
    ├── Models/
    │   └── room.py          # Modelo de dados da sala
    ├── Repository/
    │   └── roomDb.py        # Acesso ao banco de dados (SQLite + SQLAlchemy)
    └── Service/
        └── room_service.py  # Regras de negócio
```
