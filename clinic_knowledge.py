# Studio Dentistico Dottoressa Emanuela - Knowledge Base

CLINIC_INFO = {
    "name": "Studio Dentistico Dottoressa Emanuela",
    "address": "Via Roma 123, 20100 Milano, Italia",
    "phone": "+39 02 1234567",
    "email": "info@studioemanuela.it",
    "website": "www.studioemanuela.it",
    "hours": {
        "lunedi": "9:00-18:00",
        "martedi": "9:00-18:00", 
        "mercoledi": "9:00-18:00",
        "giovedi": "9:00-18:00",
        "venerdi": "9:00-18:00",
        "sabato": "9:00-13:00",
        "domenica": "Chiuso"
    },
    "emergency_hours": "Emergenze disponibili su appuntamento anche fuori orario",
    "parking": "Parcheggio gratuito disponibile",
    "accessibility": "Studio accessibile ai disabili"
}

SERVICES = {
    "odontoiatria_generale": {
        "name": "Odontoiatria Generale",
        "description": "Visite di controllo, diagnosi e trattamenti dentali di base",
        "duration": "30-60 minuti",
        "price_range": "€50-150"
    },
    "igiene_dentale": {
        "name": "Igiene Dentale e Pulizia",
        "description": "Pulizia professionale, rimozione tartaro e placca",
        "duration": "45 minuti",
        "price_range": "€80-120"
    },
    "ortodonzia": {
        "name": "Ortodonzia",
        "description": "Apparecchi fissi e mobili, allineatori trasparenti",
        "duration": "45-90 minuti",
        "price_range": "€2000-6000 (trattamento completo)"
    },
    "implantologia": {
        "name": "Implantologia",
        "description": "Impianti dentali in titanio per sostituire denti mancanti",
        "duration": "60-120 minuti",
        "price_range": "€800-2500 per impianto"
    },
    "estetica_dentale": {
        "name": "Estetica Dentale",
        "description": "Sbiancamento, faccette, ricostruzioni estetiche",
        "duration": "60-90 minuti",
        "price_range": "€200-800"
    },
    "endodonzia": {
        "name": "Endodonzia",
        "description": "Devitalizzazioni e trattamenti canalari",
        "duration": "60-90 minuti",
        "price_range": "€300-600"
    },
    "chirurgia_orale": {
        "name": "Chirurgia Orale",
        "description": "Estrazioni, chirurgia dei denti del giudizio",
        "duration": "30-60 minuti",
        "price_range": "€100-400"
    },
    "protesi": {
        "name": "Protesi Dentali",
        "description": "Protesi fisse e mobili, corone e ponti",
        "duration": "Multiple visite",
        "price_range": "€400-1500 per elemento"
    }
}

STAFF = {
    "dott_emanuela": {
        "name": "Dottoressa Emanuela",
        "title": "Odontoiatra",
        "specializations": ["Odontoiatria generale", "Estetica dentale", "Implantologia"],
        "experience": "15 anni di esperienza",
        "languages": ["Italiano", "Inglese"]
    },
    "igienista": {
        "name": "Dott.ssa Maria Rossi",
        "title": "Igienista Dentale",
        "specializations": ["Igiene orale", "Prevenzione"],
        "experience": "8 anni di esperienza"
    }
}

FAQ = {
    "quanto_costa_visita": {
        "question": "Quanto costa una visita di controllo?",
        "answer": "Una visita di controllo costa €50-80. Il prezzo può variare in base alla complessità della visita e agli eventuali esami necessari."
    },
    "accettate_assicurazioni": {
        "question": "Accettate assicurazioni sanitarie?",
        "answer": "Sì, accettiamo le principali assicurazioni sanitarie. Vi consigliamo di verificare la copertura con la vostra assicurazione prima dell'appuntamento."
    },
    "emergenze": {
        "question": "Cosa fare in caso di emergenza dentale?",
        "answer": "Per emergenze dentali chiamate il nostro numero. Offriamo appuntamenti urgenti anche fuori orario per casi di dolore acuto o traumi."
    },
    "prima_visita": {
        "question": "Cosa portare alla prima visita?",
        "answer": "Portate un documento d'identità, tessera sanitaria, eventuali radiografie precedenti e l'elenco dei farmaci che assumete."
    },
    "pagamenti": {
        "question": "Quali metodi di pagamento accettate?",
        "answer": "Accettiamo contanti, carte di credito/debito, bonifici bancari e offriamo piani di pagamento rateali per trattamenti costosi."
    },
    "bambini": {
        "question": "Visitate anche i bambini?",
        "answer": "Sì, offriamo servizi di odontoiatria pediatrica per bambini dai 3 anni in su. Creiamo un ambiente accogliente e rassicurante per i piccoli pazienti."
    },
    "anestesia": {
        "question": "Usate l'anestesia per i trattamenti?",
        "answer": "Sì, utilizziamo anestesia locale per tutti i trattamenti che potrebbero causare dolore. Offriamo anche sedazione cosciente per pazienti ansiosi."
    },
    "igiene_frequenza": {
        "question": "Ogni quanto fare la pulizia dei denti?",
        "answer": "Consigliamo una pulizia professionale ogni 6 mesi, ma la frequenza può variare in base alle condizioni individuali della bocca."
    }
}

APPOINTMENT_TYPES = {
    "visita_controllo": {
        "name": "Visita di Controllo",
        "duration": 30,
        "description": "Controllo generale dello stato di salute orale"
    },
    "igiene_dentale": {
        "name": "Igiene Dentale",
        "duration": 45,
        "description": "Pulizia professionale e rimozione tartaro"
    },
    "visita_urgente": {
        "name": "Visita Urgente",
        "duration": 30,
        "description": "Per dolori acuti o emergenze dentali"
    },
    "ortodonzia": {
        "name": "Visita Ortodontica",
        "duration": 60,
        "description": "Valutazione per apparecchi o allineatori"
    },
    "implantologia": {
        "name": "Consulenza Implantologica",
        "duration": 45,
        "description": "Valutazione per impianti dentali"
    },
    "estetica": {
        "name": "Consulenza Estetica",
        "duration": 45,
        "description": "Sbiancamento, faccette e trattamenti estetici"
    }
}

INSURANCE_INFO = {
    "accepted_insurances": [
        "Unisalute",
        "Generali",
        "Allianz Care",
        "AXA",
        "Previmedical",
        "FASI",
        "Casagit"
    ],
    "coverage_info": "La copertura varia in base al piano assicurativo. Consigliamo di verificare con la propria assicurazione prima dell'appuntamento.",
    "direct_billing": "Offriamo fatturazione diretta per alcune assicurazioni. Verificare disponibilità al momento della prenotazione."
}

PAYMENT_OPTIONS = {
    "methods": ["Contanti", "Carte di credito/debito", "Bonifico bancico", "Assegno"],
    "installments": "Piani di pagamento rateali disponibili per trattamenti superiori a €500",
    "receipts": "Rilasciamo sempre fattura sanitaria detraibile fiscalmente"
}
