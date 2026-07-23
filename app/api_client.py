import requests
import os
import logging

logger = logging.getLogger(__name__)

API_URL = os.environ.get("API_URL", "http://localhost:5001")


def buscar_agendamentos(busca=""):
    try:
        params = {"busca": busca} if busca else {}
        response = requests.get(f"{API_URL}/api/agendamentos", params=params, timeout=5)
        response.raise_for_status()
        dados = response.json()

        if not isinstance(dados, list):
            logger.error("Resposta da API em formato invalido.")
            return None, "Resposta da API em formato invalido."

        return dados, None

    except requests.ConnectionError:
        logger.error("API indisponivel.")
        return None, "Servico de agendamentos indisponivel. Tente novamente mais tarde."

    except requests.Timeout:
        logger.error("Timeout na API.")
        return None, "Servico de agendamentos demorou para responder."

    except requests.HTTPError as e:
        logger.error("Erro HTTP da API: %s", e)
        return None, "Erro ao buscar agendamentos."

    except Exception as e:
        logger.error("Erro inesperado: %s", e)
        return None, "Erro inesperado ao buscar agendamentos."