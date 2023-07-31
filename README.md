# dio-lab-sistema-bancario

Resolução do lab "Criando um Sistema Bancário com Python", do Bootcamp **"Potência Tech powered by iFood | Ciência de Dados"** da [dio](https://www.dio.me/bootcamp/potencia-tech-powered-ifood-ciencias-de-dados-com-python).

**Desafio:** Deve-se criar um sistema bancário com as seguintes características:

1. Possui apenas 3 operações: Depósito, Saque e Extrato.
2. Apenas deve-se depositar valores positivos.
3. Não deve-se preocupar com as contas dos usuários (a princípio será considerado apenas 1 usuário).
4. É permitido realizar até 3 saques diários com limite máximo de R$ 500,00 por saque. Se não houver saldo em conta o sistema deve exibir uma mensagem que não foi possível realizar o saque.
5. Todos os depósitos e saques serão exibidos no extrato, assim como o saldo atual da conta. Se o extrato estiver em branco deve-se exibir: "Não foram realizadas movimentações". Além disso, os valores devem ser exibidos no formato: R$ XXX.XX.
