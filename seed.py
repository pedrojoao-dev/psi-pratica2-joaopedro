from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(nome = 'Noberto',pais = 'portugal')
    autor2 = Autor(nome = 'jeizon',pais =  'Caicó') 
    autor3 = Autor(nome = 'pedro', pais = 'inglaterra')

    session.add_all([autor1,autor2,autor3])
    session.commit()
    # TODO: crie pelo menos 6 livros.
    livros = [
       Livro(titulo ='amor',ano= 1989 , disponivel = True,autor_id = autor1.id),
       Livro(titulo ='amor2',ano= 1990 , disponivel = True,autor_id = autor1.id),
       Livro(titulo ='final feliz',ano= 1989 , disponivel = True,autor_id = autor2.id),
       Livro(titulo ='que nem maré',ano= 1990 , disponivel = True,autor_id = autor2.id),
       Livro(titulo ='monalisa',ano= 1949 , disponivel = True,autor_id = autor2.id),
       Livro(titulo ='samurai',ano= 1989 , disponivel = True,autor_id = autor3.id)

    ]
    for l in livros:
        session.add(l)

    session.commit()
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    pass
