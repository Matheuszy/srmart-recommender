from models.cliente import Cliente
from models.sessao import SessaoCliente

from markov.comportamento import CadeiaMarkov
from bayes.compra import RedeBayesiana
from decision.objetivo import MotorDecisao

from astar.recomendador import Recomendador

from data.produtos import produto_aleatorio


def main():

    cliente = Cliente(
        historico=1,
        tempo_site=1,
        clicou_promocao=1
    )

    sessao = SessaoCliente(
        cliente=cliente,
        estado_atual="Visitando",
        produto_atual=produto_aleatorio()
    )

    print("=" * 60)
    print("SMART PRODUCT RECOMMENDER")
    print("=" * 60)

    print(f"\nProduto atual: {sessao.produto_atual}")
    print(f"Estado atual: {sessao.estado_atual}")

    # -----------------------------
    # Cadeia de Markov
    # -----------------------------

    markov = CadeiaMarkov()

    novo_estado = markov.prever(
        sessao.estado_atual
    )

    sessao.atualizar_estado(
        novo_estado
    )

    # -----------------------------
    # Rede Bayesiana
    # -----------------------------

    bayes = RedeBayesiana()

    probabilidade = bayes.calcular(
        sessao.cliente
    )

    # -----------------------------
    # Motor de decisão
    # -----------------------------

    motor = MotorDecisao()

    objetivo = motor.objetivo(
        sessao.estado_atual,
        sessao.produto_atual
    )

    if objetivo is None:

        print(f"\nNovo estado: {sessao.estado_atual}")
        print("\nNenhuma recomendação disponível.")
        return

    fator = motor.fator(
        sessao.estado_atual
    )

    # -----------------------------
    # Algoritmo A*
    # -----------------------------

    recomendador = Recomendador(
        probabilidade,
        fator
    )

    caminho = recomendador.buscar(
        sessao.produto_atual,
        objetivo
    )

    print(f"\nNovo estado previsto: {sessao.estado_atual}")
    print(f"Probabilidade de compra: {probabilidade:.2%}")
    print(f"Objetivo da recomendação: {objetivo.nome}")
    print(f"Fator heurístico: {fator}")

    print("\nMelhor caminho encontrado")
    print("-" * 30)

    if not caminho:

        print("Nenhum caminho encontrado.")

    else:

        for i, produto in enumerate(caminho, start=1):

            print(f"{i}. {produto}")


if __name__ == "__main__":
    main()