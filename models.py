from __future__ import annotations
from typing import List


from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# TODO: crie o modelo Autor.
# Campos: id, nome, pais.
# Relacionamento: livros.
class Autor(Base):
    __tablename__ = 'autores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    pais: Mapped[str] = mapped_column(String(100), nullable=True)

    livros: Mapped[list[Livro]] = relationship(back_populates='autor')

# TODO: crie o modelo Livro.
# Campos: id, titulo, ano, autor_id.
# Relacionamento: autor.
class Livro(Base):
    __tablename__ = 'livros'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
    ano: Mapped[int] = mapped_column(nullable=True,)
    autor_id: Mapped[int] = mapped_column(ForeignKey('autores.id'))

    autor: Mapped[Autor] = relationship(back_populates='livros')


