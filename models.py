from banco import bd


class Presenca:
    def __init__(self, email, presenca, resposta, comentarios):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentarios = comentarios

    def gravar(self):
        sql = '''insert into tb_presenca (email, presenca, resposta,
                 comentarios) values (?, ?, ?, ?)'''
        valor_01 = self.email
        valor_02 = self.presenca
        valor_03 = self.resposta
        valor_04 = self.comentarios
        bd().execute(sql, [valor_01, valor_02, valor_03, valor_04])
        bd().commit()

    @staticmethod
    def recupera_todos():
        
        sql = '''select email, presenca, resposta, comentarios from
                 tb_presenca order by id desc'''
        cur = bd().execute(sql)
        
        presencas = []
        
        for email_f, presenca_f, resposta_f, comentarios_f in cur.fetchall():
            presenca = Presenca(email_f, presenca_f, resposta_f, comentarios_f)
            presencas.append(presenca)

        return presencas
