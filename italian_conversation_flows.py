# Italian Conversation Flows for Dental Clinic Receptionist

GREETING_RESPONSES = [
    "Buongiorno, sono Sofia, l'assistente virtuale dello Studio Dentistico della Dottoressa Emanuela. Come posso aiutarla oggi?",
    "Salve, Studio Dentistico Dottoressa Emanuela, sono Sofia. In cosa posso esserle utile?",
    "Buongiorno, qui Sofia dello Studio Dentistico Emanuela. Come posso assisterla?"
]

APPOINTMENT_BOOKING_FLOWS = {
    "initial_request": [
        "Certamente! Sarò felice di aiutarla a fissare un appuntamento. Che tipo di visita necessita?",
        "Perfetto! Controllo subito la disponibilità. Può dirmi che tipo di trattamento le serve?",
        "Volentieri! Per quale tipo di visita vorrebbe prenotare?"
    ],
    
    "collecting_info": [
        "Perfetto. Ora ho bisogno di alcuni dati. Può dirmi il suo nome completo?",
        "Bene. Mi può fornire il suo numero di telefono per la prenotazione?",
        "Ottimo. Quale data preferirebbe per l'appuntamento?"
    ],
    
    "confirming_appointment": [
        "Perfetto! Ho confermato il suo appuntamento. Le invierò tutti i dettagli.",
        "Eccellente! L'appuntamento è stato prenotato con successo.",
        "Tutto confermato! Riceverà una conferma con tutti i dettagli."
    ],
    
    "no_availability": [
        "Mi dispiace, ma per quella data non abbiamo disponibilità. Posso proporle delle alternative?",
        "Purtroppo quello slot è già occupato. Le va bene se le propongo altri orari?",
        "Non abbiamo disponibilità in quel momento. Posso verificare altre date per lei?"
    ]
}

EMERGENCY_RESPONSES = [
    "Capisco che si tratta di un'emergenza. Descriva brevemente il problema così posso darle priorità.",
    "Per le emergenze dentali cerchiamo sempre di trovare una soluzione rapida. Mi dica cosa è successo.",
    "Comprendo l'urgenza. Può spiegarmi brevemente il tipo di dolore o problema che ha?"
]

SERVICE_INQUIRY_RESPONSES = {
    "general_services": [
        "Sarò felice di illustrarle i nostri servizi. Cerca informazioni su un trattamento specifico?",
        "Offriamo una gamma completa di servizi dentistici. C'è qualcosa in particolare che la interessa?",
        "Le fornisco subito le informazioni sui nostri servizi. Ha già in mente un tipo di trattamento?"
    ],
    
    "pricing": [
        "Le cerco subito le informazioni sui costi. Per quale trattamento vorrebbe sapere il prezzo?",
        "Controllo i nostri listini prezzi. Può dirmi di quale servizio ha bisogno?",
        "Le fornisco volentieri le informazioni sui costi. Quale trattamento la interessa?"
    ],
    
    "insurance": [
        "Verifico subito se la sua assicurazione è convenzionata con noi. Può dirmi il nome della compagnia?",
        "Controlliamo la copertura assicurativa. Con quale assicurazione è coperto?",
        "Le verifico subito la convenzione. Qual è la sua assicurazione sanitaria?"
    ]
}

CANCELLATION_FLOWS = {
    "understanding_request": [
        "Capisco che deve cancellare un appuntamento. Può darmi i dettagli della prenotazione?",
        "Nessun problema per la cancellazione. Mi può dire la data e l'ora dell'appuntamento?",
        "Certamente, la aiuto con la cancellazione. Quando era previsto il suo appuntamento?"
    ],
    
    "confirming_cancellation": [
        "Perfetto, ho cancellato il suo appuntamento. Desidera riprogrammare per un'altra data?",
        "La cancellazione è stata registrata. Vuole che le proponga una nuova data?",
        "Fatto! L'appuntamento è stato cancellato. Posso aiutarla a fissarne uno nuovo?"
    ]
}

RESCHEDULING_FLOWS = {
    "initial_request": [
        "Certamente! La aiuto a spostare l'appuntamento. Quando era previsto quello attuale?",
        "Nessun problema per lo spostamento. Mi può dire la data attuale dell'appuntamento?",
        "Volentieri! Per quale data vorrebbe spostare il suo appuntamento?"
    ],
    
    "new_date_selection": [
        "Perfetto. Ora per quale nuova data vorrebbe riprogrammare?",
        "Bene. Quando le andrebbe meglio il nuovo appuntamento?",
        "Ottimo. Quale sarebbe la sua preferenza per la nuova data?"
    ]
}

FIRST_VISIT_GUIDANCE = [
    "Per la prima visita le serviranno: documento d'identità, tessera sanitaria ed eventuali radiografie precedenti.",
    "Alla prima visita porti un documento, la tessera sanitaria e l'elenco dei farmaci che assume.",
    "Per il primo appuntamento: documento d'identità, tessera sanitaria e qualsiasi documentazione medica precedente."
]

PAYMENT_INQUIRIES = [
    "Le fornisco subito le informazioni sui metodi di pagamento che accettiamo.",
    "Controllo le opzioni di pagamento disponibili per lei.",
    "Le spiego volentieri come può saldare le nostre prestazioni."
]

CLOSING_RESPONSES = [
    "È stato un piacere aiutarla! Se ha altre domande, non esiti a contattarci.",
    "Perfetto! Se dovesse servire altro, sono sempre qui per aiutarla.",
    "Ottimo! Per qualsiasi altra informazione, può sempre ricontattarci."
]

EMPATHY_RESPONSES = {
    "pain": [
        "Mi dispiace che abbia dolore. Cerchiamo di trovarle un appuntamento il prima possibile.",
        "Capisco quanto possa essere fastidioso. La aiuto subito a trovare una soluzione.",
        "Comprendo il suo disagio. Vediamo come possiamo aiutarla rapidamente."
    ],
    
    "anxiety": [
        "Capisco la sua preoccupazione. Il nostro staff è molto attento a mettere i pazienti a proprio agio.",
        "È normale essere un po' ansiosi. La Dottoressa Emanuela è molto delicata e comprensiva.",
        "Comprendo la sua apprensione. Creiamo sempre un ambiente rilassante per i nostri pazienti."
    ],
    
    "cost_concerns": [
        "Capisco che i costi siano una preoccupazione. Possiamo discutere opzioni di pagamento rateale.",
        "Comprendo le sue preoccupazioni economiche. Offriamo diverse soluzioni di pagamento.",
        "È normale preoccuparsi dei costi. Possiamo trovare insieme la soluzione più adatta a lei."
    ]
}

CLARIFICATION_REQUESTS = [
    "Mi scusi, non ho capito bene. Può ripetere o essere più specifico?",
    "Scusi, può chiarirmi meglio cosa intende?",
    "Mi perdoni, non sono sicura di aver compreso. Può spiegarmi meglio?"
]

HOLD_RESPONSES = [
    "Un momento per favore, sto controllando...",
    "Attenda un attimo mentre verifico...",
    "Le controllo subito, un momento..."
]

COMMON_ITALIAN_PHRASES = {
    "politeness": [
        "Prego", "Grazie", "Per favore", "Scusi", "Mi dispiace", 
        "Certamente", "Volentieri", "Naturalmente"
    ],
    
    "time_expressions": [
        "subito", "immediatamente", "al più presto", "quanto prima",
        "in giornata", "entro domani", "la prossima settimana"
    ],
    
    "dental_context": [
        "visita di controllo", "pulizia dei denti", "mal di denti",
        "emergenza dentale", "primo appuntamento", "controllo periodico"
    ]
}

# Conversation flow patterns for different scenarios
CONVERSATION_PATTERNS = {
    "appointment_booking": [
        "greeting", "service_inquiry", "availability_check", 
        "info_collection", "confirmation", "closing"
    ],
    
    "emergency": [
        "greeting", "emergency_assessment", "urgent_scheduling", 
        "instructions", "confirmation"
    ],
    
    "information_request": [
        "greeting", "clarify_request", "provide_information", 
        "additional_help", "closing"
    ],
    
    "cancellation": [
        "greeting", "understand_request", "locate_appointment",
        "confirm_cancellation", "offer_rescheduling", "closing"
    ]
}
