from models.cliente import Cliente
from models.sessao import SessaoCliente

from markov.comportamento import CadeiaMarkov
from bayes.compra import RedeBayesiana
from decision.objetivo import MotorDecisao
from astar.recomendador import Recomendador

from data.produtos import produto_aleatorio


class RecommendationService:

    def executar(
        self,
        historico,
        tempo_site,
        clicou_promocao,
        estado
    ):

        cliente = Cliente(
            historico,
            tempo_site,
            clicou_promocao
        )

        sessao = SessaoCliente(
            cliente,
            estado,
            produto_aleatorio()
        )

        markov = CadeiaMarkov()

        sessao.atualizar_estado(

            markov.prever(
                sessao.estado_atual
            )

        )

        bayes = RedeBayesiana()

        prob = bayes.calcular(
            sessao.cliente
        )

        motor = MotorDecisao()

        objetivo = motor.objetivo(
            sessao.estado_atual,
            sessao.produto_atual
        )

        if objetivo is None:

            return {

                "produto_atual": sessao.produto_atual.nome,
                "estado_previsto": sessao.estado_atual,
                "probabilidade_compra": prob,
                "objetivo": None,
                "recomendacoes": []

            }

        recomendador = Recomendador(

            prob,

            motor.fator(
                sessao.estado_atual
            )

        )

        caminho = recomendador.buscar(

            sessao.produto_atual,

            objetivo

        )

        return {

            "produto_atual": sessao.produto_atual.nome,

            "estado_previsto": sessao.estado_atual,

            "probabilidade_compra": prob,

            "objetivo": objetivo.nome,

            "recomendacoes": [

                {

                    "nome": p.nome,

                    "categoria": p.categoria

                }

                for p in caminho

            ]

        }