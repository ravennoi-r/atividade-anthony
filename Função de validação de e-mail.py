def email_valido(email: str) -> bool:
    email = email.strip()

    if "@" not in email:
        return False

    partes = email.split("@")

    if len(partes) != 2:
        return False

    dominio = partes[1]

    if "." not in dominio:
        return False

    return True


print(email_valido("aluno@ifpi.edu.br"))
print(email_valido("aluno.ifpi.edu.br"))
print(email_valido("aluno@ifpi"))