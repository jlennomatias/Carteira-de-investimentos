App FinanceWallet

app para controle de ativos

Functionalidades:
    . Qualquer pessoa poderá acompanhar o preço atual dos ativos
    . Qualquer pessoa poderá cadastrar as compras e vendas dos ativos
    . Uma pessoa tem:
        . nome
        . cpf
        . senha
    . Um ativo tem:
        . nome
        . código
        . preço
        . fotos
    . Uma carteira tem:
        . pessoa
        . ativo
        . quantidade
        . valor
        . tipo de operação
        . data de operação
    . A pessoa poderá acompanhar seus ativos em tempo real:
        . status(porcentagem de ganho e perda)
        . preço médio
        . dividendos recebidos
        . valor do ativo com o desconto do dividendos

Dependencias:
    . Python + FastAPI
    . Será uma API REST
    . Banco de dados: Postgresql e/ou Mongodb
    Docker para o banco de dados