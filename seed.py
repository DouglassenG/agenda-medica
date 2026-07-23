from app.models import init_db, create_user


def seed():
    print("Criando tabela de usuarios...")
    init_db()

    print("Inserindo usuario de teste...")
    created = create_user(
        username="admin",
        email="admin@agenda.com",
        password="admin123"
    )

    if created:
        print("Usuario de teste criado com sucesso!")
    else:
        print("Usuario de teste ja existe, pulando...")

    print("Seed finalizado.")


if __name__ == "__main__":
    seed()