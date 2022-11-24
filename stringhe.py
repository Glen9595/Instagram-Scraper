##########################################################################################################################
#                                                                                                                        #
#   STRINGHE.PY                                                                                                          #
#   __________________________________________________________________________________________________________________   #
#  | In questo file sono presenti una serie di variabili contenenti messaggi che verranno mostrati a video per        |  #
#  | ottenere una lettura più scorrevole ed una comprensione più immediata visualizzando il progetto da terminale.    |  #
#  |__________________________________________________________________________________________________________________|  #
#                                                                                                                        #
##########################################################################################################################


t0='\n\n \t\t\t\t\t  ▀█▀ ░█▄─░█ ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▄▀█   ░█▀▀▀█ ░█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█'
t1='\t\t\t\t\t  ░█─ ░█░█░█ ─▀▀▀▄▄ ─░█── ░█▄▄█ ░█─▄▄ ░█▄▄▀ ░█▄▄█ ░█░█░█   ─▀▀▀▄▄ ░█─── ░█▄▄▀ ░█▄▄█ ░█▄▄█ ░█▀▀▀ ░█▄▄▀'
t2='\t\t\t\t\t  ▄█▄ ░█──▀█ ░█▄▄▄█ ─░█── ░█─░█ ░█▄▄█ ░█─░█ ░█─░█ ░█──░█   ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█─░█ ░█─── ░█▄▄▄ ░█─░█'

te1='\nBenvenuto su Instagram Scraper, una applicazione a linea di comando che ti permette di effettuare la raccolta ed il download di post ed informzioni di profili Instagram.'
te2='\nPer garantire la sicurezza del tuo account instagram, è prima necessario effettuare l accesso su Instagram da browser Firefox. \nUna volta effettuato, procedi inserendo il tuo nome su Instagram.\n'
te3='\nI comandi primari ti permettono di effettuare il download di elementi presenti sul profilo Instagram. Possono essere utilizzati da soli'

te4='\n░ profileinfo \t\t\tEffettua il download della biografia, il numero di followers, il numero di utenti seguiti e a somma del numero dei post del profilo'
te8='░ posts \t\t\tEffettua il download di tutti i post pubblicati dal profilo'
te9='░ tagged \t\t\tEffettua il download di tutti i post in cui il profilo è stato taggato'
te10='░ stories \t\t\tSe presente, effettua il download delle stories attuali'
te11='░ hl \t\t\t\tSe presente, effettua il download degli highlights del profilo'

te12='\nQuesti comandi, inseriti di seguito a comandi specifici, ci permettono di ottenere delle infomazioni aggiuntive:\n'

te13='░ metadata \t\t\tAcquisisce metadati, usabile con i comandi posts | tagged | hl |'
te15='░ timeperiod \t\t\tEffettua il download di posts in uno specifico intervallo temporale, usabile col comando | posts | tagged |'


s1= '░░ Inserisci l username del tuo profilo instagram:'
s2= '\n░░ Inserisci il profilo instagram da cui raccogliere dati:'
s3= '\n░░ 1 - DOWNLOAD MEDIA:'
s5= '\n\n░░ 2 - COMANDI AGGIUNTIVI:'
s6= '\n░░ Inserire comando. Se più di uno, inserire i comandi separati da uno spazio.'
s7= '\n░░ Vuoi avviare nuovamente lo scraper? (S/N) '

dh1='\n|| Digest Sha-256:'
dh2='\n|| Digest Sha-512:'
inf='\n\n|| Informazioni:\n'
path='\n|| Selezionare un percorso per salvare i dati, se lo si desidera, altrimenti premere Invio:'

spazio1='\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ VERIFICATO!'
spazio2='\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ SALVATAGGIO EFFETTUATO!'


g1= '░░ Biografia:'
g2= '░░ Followers:'
g3= '░░ Numero di posts pubblicati:'
g4= '░░ Numero profili seguiti:'
g5= '░░ Sto effettuando il download di tutti i post pubblicati dal profilo nella cartella '
g6= 'Likes: '
g7= 'Data di pubblicazione: '
g8= 'Caption: '
g9= 'Utenti taggati: '
g10= 'Luogo (''None'' se non definito): '
g11= '░░ Sto effettuando il download di tutti i post in cui il profilo è taggato nella nuova cartella '
g12= '░░ Sto effettuando il download di tutte le storie in una nuova cartella'
g13= '░░ Sto effettuando il download di tutte le highlights in una nuova cartella '
g14= 'Titoli: '
g15= 'Url della cover della highlights: '



r1= 'Errore nella pubblicazione dei dati!'

p1= '\n\n\t\t\t\t\t\t\t\t' + '|░ |░░| ░| CONNESSIONE AL TUO PROFILO INSTAGRAM |░ |░░| ░|'
p2= '\n\n\t\t\t\t\t\t\t\t\t' + '|░ |░░| ░| SCRAPING DEL PROFILO |░ |░░| ░|'