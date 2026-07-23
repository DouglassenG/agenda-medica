from flask import Flask, jsonify, request

app = Flask(__name__)

AGENDAMENTOS = [
    {
        "id": 1,
        "paciente": "Maria Silva",
        "cpf": "123.456.789-00",
        "medico": "Dr. Carlos Souza",
        "especialidade": "Cardiologia",
        "data": "2026-07-23",
        "horario": "08:00",
        "convenio": "Unimed",
        "status": "Confirmado"
    },
    {
        "id": 2,
        "paciente": "Joao Santos",
        "cpf": "987.654.321-00",
        "medico": "Dra. Ana Lima",
        "especialidade": "Dermatologia",
        "data": "2026-07-23",
        "horario": "09:30",
        "convenio": "SulAmerica",
        "status": "Aguardando"
    },
    {
        "id": 3,
        "paciente": "Pedro Oliveira",
        "cpf": "456.789.123-00",
        "medico": "Dr. Carlos Souza",
        "especialidade": "Cardiologia",
        "data": "2026-07-23",
        "horario": "10:00",
        "convenio": "Bradesco Saude",
        "status": "Confirmado"
    },
    {
        "id": 4,
        "paciente": "Ana Costa",
        "cpf": "321.654.987-00",
        "medico": "Dra. Lucia Ferreira",
        "especialidade": "Pediatria",
        "data": "2026-07-24",
        "horario": "14:00",
        "convenio": "Amil",
        "status": "Cancelado"
    },
    {
        "id": 5,
        "paciente": "Lucas Mendes",
        "cpf": "654.321.987-00",
        "medico": "Dr. Roberto Alves",
        "especialidade": "Ortopedia",
        "data": "2026-07-24",
        "horario": "15:30",
        "convenio": "Unimed",
        "status": "Confirmado"
    },
    {
        "id": 6,
        "paciente": "Fernanda Rocha",
        "cpf": "789.123.456-00",
        "medico": "Dra. Ana Lima",
        "especialidade": "Dermatologia",
        "data": "2026-07-25",
        "horario": "08:30",
        "convenio": "Particular",
        "status": "Aguardando"
    }
]


@app.route("/api/agendamentos", methods=["GET"])
def listar_agendamentos():
    busca = request.args.get("busca", "").strip().lower()

    if not busca:
        return jsonify(AGENDAMENTOS)

    resultados = [
        a for a in AGENDAMENTOS
        if busca in a["paciente"].lower()
        or busca in a["cpf"]
        or busca in a["medico"].lower()
    ]

    return jsonify(resultados)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)