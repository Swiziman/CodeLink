data = {
        'data_hora': registro.data_hora,
        'alarme_id': registro.alarme_id,
        'raspberry_id': registro.raspberry_id,
        'dispositivo_id': registro.dispositivo_id,
        'closed': registro.closed
}

response, error = client.table('registro_movimentacao').insert(data).execute()

    if error:
        print("Erro ao inserir registro no Supabase:", error)
    else:
        print("Registro inserido com sucesso no Supabase")

def atualizar_registro_no_supabase(registro):
    client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

    data = {
        'data_hora': registro.data_hora,
        'alarme_id': registro.alarme_id,
        'raspberry_id': registro.raspberry_id,
        'dispositivo_id': registro.dispositivo_id,
        'closed': registro.closed
    }

    response, error = client.table('registro_movimentacao').upsert(data).execute()

    if error:
        print("Erro ao atualizar registro no Supabase:", error)
    else:
        print("Registro atualizado com sucesso no Supabase")