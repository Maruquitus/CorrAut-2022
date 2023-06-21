import pickle

def novaAvaliaçao(serie, curso, questoes, alunos, avaliacao, dados, matriz, pasta):
    informações = {'série':serie,
                    'curso':curso,
                    'questões':questoes,
                    'alunos':alunos,
                    'avaliacao':avaliacao,
                    'dados':dados,
                    'matriz': matriz}

    with open(pasta + f'/{avaliacao}.dat', 'wb') as handle:
            pickle.dump(informações, handle, protocol=pickle.HIGHEST_PROTOCOL)