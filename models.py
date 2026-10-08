from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable = True)
    pais: Mapped[str] = mapped_column(nullable = True)
    livros: Mapped[list['Livro']] = relationship( back_populates = 'autor')

    # TODO: relacione Autor com Livro usando relationship e back_populates.


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable = True)
    ano: Mapped[int] = mapped_column(nullable = True)
    disponivel: Mapped[bool] = mapped_column(default = True)

    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    autor: Mapped['Autor'] = relationship( back_populates = 'livros')


    # TODO: adicione o campo disponivel, com valor padrão True.
    # TODO: relacione Livro com Autor usando relationship e back_populates.
