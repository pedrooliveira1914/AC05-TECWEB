-- Criando a tabela presença

drop table if exists tb_presenca;
create table tb_presenca (
  id integer primary key autoincrement,
  email string not null,
  presenca string not null,
  resposta string not null,
  comentarios string not null
);