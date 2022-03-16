endereco = "Rua da Flores 72, apartamento 1002, Rio de Janeiro, RJ, 234407gfr"

import re

# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[^abc]{3}")

busca = padrao.search(endereco) #Math
if busca:
    cep = busca.group()
    print(cep)