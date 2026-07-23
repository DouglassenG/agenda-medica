from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import authenticate_user
from app.api_client import buscar_agendamentos
import logging

logger = logging.getLogger(__name__)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET"])
def index():
    if session.get("user_id"):
        return redirect(url_for("auth.agenda"))
    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_input = request.form.get("login", "").strip()
        password = request.form.get("password", "").strip()

        if not login_input or not password:
            flash("Preencha todos os campos.", "error")
            return render_template("login.html"), 400

        try:
            user = authenticate_user(login_input, password)
        except ConnectionError:
            logger.error("Falha na conexao com o banco de dados durante login.")
            flash("Erro interno. Tente novamente mais tarde.", "error")
            return render_template("login.html"), 500

        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            logger.info("Login realizado: %s", user["username"])
            return redirect(url_for("auth.agenda"))

        flash("Usuario ou senha invalidos.", "error")
        return render_template("login.html"), 401

    return render_template("login.html")


@auth_bp.route("/agenda", methods=["GET"])
def agenda():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    busca = request.args.get("busca", "").strip()
    dados, erro = buscar_agendamentos(busca)

    return render_template(
        "agenda.html",
        agendamentos=dados,
        erro=erro,
        busca=busca,
        username=session["username"]
    )


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logout realizado com sucesso.", "success")
    return redirect(url_for("auth.login"))