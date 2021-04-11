def caixa(sale, pay):
    troco = pay - sale
    bank_note = [100, 50, 20, 10, 5, 2, 1]
    note_list= []
    while troco > 0:
        def troco_calculo(troco, nota):
            """Calcula a quantidade de uma determinada nota ira ter e o resto do troco é retorna ambos"""
            banknote_quant = troco // nota
            troco =  troco % nota 
            return banknote_quant, troco


        def add_note_inlist(note_quantity, note):
            """verifica se a quantidade de uma nota e maior que zero e caso for verdadeiro a coloca na lista de retorno"""
            if note_quantity > 0:
                note_list.append(f"{note_quantity} notas de {note}R$" )
            
        
        for note in bank_note:
            note_quantity, troco = troco_calculo(troco, note)
            add_note_inlist(note_quantity, note)
        return note_list

# copyright FideumaEgua © 2021