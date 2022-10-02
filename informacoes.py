Base = declarative_base()
class EMPREGADO(Base):
    __tablename__ = "empregados"
    id_empregado = Column(Integer, primary_key=True)
    nome_empregado = Column(String(200), nullable=False)
class CLIENTE(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True)
    nome_cliente = Column(String(200), nullable=False)
class PASTEL(Base):
    __tablename__ = "pasteis"
    id_pastel = Column(Integer, primary_key=True)
    descrição = Column(String(200), nullable=False)
class VENDA(Base);
    __tablename__ = "pasteis_vendidos"
    id_pastel = Column(Integer, Foreign_key=True, references=pastel(id_pastel)
    venda = Column(Integer, nullable=False)
    id_empregado = Column(Integer, Foreign_key=True, references=empregados(id_empregado))
Base.metadata.drop.all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
empregados = [empregado(
    id_empregado = "1",
    nome_empregado = "joão da Silva")]
clientes = [cliente(
    id_cliente = "5",
    nome_cliente = "Mariana Guimalhaes")]
pasteis = [pastel(
    id_pastel = "9",
    descricao = "pastel de carne moída")]
pasteis_vendidos = [venda(
    id_pastel = (foreing_key, references=pastel(id_pastel)
    venda = "63",
    id_empregado = (foreing_key=True, references=empregados(id_empregado)]
with Session.begin() as session:
    for empregado in empregados:
        session.add(empregado)
with Session.begin as session:
    for cliente in clientes:
        session.add(cliente)
with Session.begin() as session
    for pastel in pasteis:
        session.add(pastel)