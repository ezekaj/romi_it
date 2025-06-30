# Italian Dental Terminology and Training Data for Emanuela's Dental Clinic

ITALIAN_DENTAL_TERMINOLOGY = {
    # Basic dental terms
    "dente": "tooth",
    "denti": "teeth", 
    "bocca": "mouth",
    "gengive": "gums",
    "lingua": "tongue",
    "mascella": "jaw",
    "mandibola": "lower jaw",
    "palato": "palate",
    "saliva": "saliva",
    
    # Dental procedures
    "pulizia": "cleaning",
    "igiene dentale": "dental hygiene",
    "otturazione": "filling",
    "estrazione": "extraction",
    "devitalizzazione": "root canal",
    "endodonzia": "endodontics",
    "impianto": "implant",
    "protesi": "prosthesis",
    "corona": "crown",
    "ponte": "bridge",
    "apparecchio": "braces",
    "ortodonzia": "orthodontics",
    "sbiancamento": "whitening",
    "detartrasi": "scaling",
    "sigillatura": "sealant",
    
    # Dental problems
    "carie": "cavity",
    "mal di denti": "toothache",
    "dolore": "pain",
    "gonfiore": "swelling",
    "sanguinamento": "bleeding",
    "sensibilità": "sensitivity",
    "infezione": "infection",
    "ascesso": "abscess",
    "tartaro": "tartar",
    "placca": "plaque",
    "alitosi": "bad breath",
    
    # Appointment types
    "visita": "visit",
    "controllo": "check-up",
    "emergenza": "emergency",
    "urgenza": "urgency",
    "consulenza": "consultation",
    "preventivo": "estimate",
    
    # Time expressions
    "appuntamento": "appointment",
    "prenotazione": "booking",
    "disponibilità": "availability",
    "orario": "schedule",
    "mattina": "morning",
    "pomeriggio": "afternoon",
    "sera": "evening"
}

COMMON_PATIENT_PHRASES = [
    # Appointment requests
    "Vorrei fissare un appuntamento",
    "Posso prenotare una visita?",
    "Quando siete disponibili?",
    "Ho bisogno di una visita urgente",
    "Vorrei fare una pulizia dei denti",
    "Devo fare un controllo",
    
    # Pain/emergency expressions
    "Ho mal di denti",
    "Mi fa molto male",
    "È un'emergenza",
    "Ho un dolore forte",
    "Mi si è rotto un dente",
    "Ho perso un'otturazione",
    
    # Information requests
    "Quanto costa?",
    "Accettate la mia assicurazione?",
    "Dove siete?",
    "Che orari fate?",
    "Come posso pagare?",
    "È la prima volta che vengo",
    
    # Cancellation/rescheduling
    "Devo cancellare l'appuntamento",
    "Posso spostare la visita?",
    "Non posso venire",
    "Vorrei cambiare data",
]

RECEPTIONIST_RESPONSES = [
    # Greetings
    "Buongiorno, Studio Dentistico Dottoressa Emanuela",
    "Salve, sono Sofia, come posso aiutarla?",
    "Buonasera, in cosa posso esserle utile?",
    
    # Appointment booking
    "Controllo subito la disponibilità",
    "Che tipo di visita necessita?",
    "Per quando vorrebbe l'appuntamento?",
    "Mi può dire il suo nome?",
    "Qual è il suo numero di telefono?",
    
    # Confirmation
    "Perfetto, ho confermato l'appuntamento",
    "Tutto a posto, ci vediamo allora",
    "Le invio una conferma",
    
    # Information providing
    "Le spiego i nostri servizi",
    "I nostri orari sono...",
    "Accettiamo queste assicurazioni...",
    "I costi sono...",
    
    # Empathy
    "Capisco il suo dolore",
    "Cerchiamo di trovarle posto subito",
    "Non si preoccupi, la aiutiamo",
]

CONVERSATION_EXAMPLES = [
    {
        "scenario": "Prenotazione visita di controllo",
        "conversation": [
            {"speaker": "paziente", "text": "Buongiorno, vorrei fissare un appuntamento per una visita di controllo"},
            {"speaker": "sofia", "text": "Buongiorno! Certamente, controllo subito la disponibilità. Per quando vorrebbe l'appuntamento?"},
            {"speaker": "paziente", "text": "La prossima settimana, se possibile"},
            {"speaker": "sofia", "text": "Perfetto. Abbiamo disponibilità martedì alle 10:30 o giovedì alle 15:00. Quale preferisce?"},
            {"speaker": "paziente", "text": "Martedì alle 10:30 va bene"},
            {"speaker": "sofia", "text": "Ottimo! Mi può dire il suo nome completo e numero di telefono per la prenotazione?"}
        ]
    },
    {
        "scenario": "Emergenza dentale",
        "conversation": [
            {"speaker": "paziente", "text": "Ho un forte mal di denti, è un'emergenza"},
            {"speaker": "sofia", "text": "Mi dispiace per il dolore. Capisco che sia urgente. Può descrivermi brevemente il tipo di dolore?"},
            {"speaker": "paziente", "text": "È un dolore pulsante, molto forte, non riesco a dormire"},
            {"speaker": "sofia", "text": "Comprendo. Cerchiamo di trovarle un appuntamento urgente. Può venire oggi pomeriggio alle 16:30?"},
            {"speaker": "paziente", "text": "Sì, perfetto, ci sarò"},
            {"speaker": "sofia", "text": "Benissimo. Nel frattempo, può prendere un antidolorifico se non ha allergie. Ci vediamo alle 16:30."}
        ]
    },
    {
        "scenario": "Richiesta informazioni servizi",
        "conversation": [
            {"speaker": "paziente", "text": "Vorrei sapere quanto costa uno sbiancamento"},
            {"speaker": "sofia", "text": "Certamente! Le fornisco subito le informazioni sui nostri trattamenti estetici. Lo sbiancamento professionale costa tra 200 e 400 euro, a seconda del tipo di trattamento."},
            {"speaker": "paziente", "text": "Accettate assicurazioni?"},
            {"speaker": "sofia", "text": "Sì, siamo convenzionati con le principali assicurazioni. Può dirmi con quale compagnia è assicurato?"},
            {"speaker": "paziente", "text": "Unisalute"},
            {"speaker": "sofia", "text": "Perfetto! Unisalute è tra le nostre convenzioni. Le consiglio di verificare la copertura per i trattamenti estetici prima dell'appuntamento."}
        ]
    }
]

TRAINING_PROMPTS = [
    {
        "context": "Paziente chiama per prenotare",
        "input": "Vorrei un appuntamento per mio figlio di 8 anni",
        "expected_response": "Certamente! Offriamo servizi di odontoiatria pediatrica. Che tipo di visita necessita il bambino? È la prima volta che viene da noi?"
    },
    {
        "context": "Paziente ha dolore",
        "input": "Mi fa male un dente da tre giorni",
        "expected_response": "Mi dispiace per il dolore che sta provando. È importante che la visitiamo presto. Può descrivermi il tipo di dolore? È continuo o solo quando mastica?"
    },
    {
        "context": "Richiesta costi",
        "input": "Quanto costa una pulizia dei denti?",
        "expected_response": "Una seduta di igiene dentale costa tra 80 e 120 euro, a seconda della complessità. La durata è di circa 45 minuti. Desidera prenotare?"
    }
]

ITALIAN_GRAMMAR_PATTERNS = {
    "formal_address": [
        "Lei", "Sua", "Suo", "Le", "La", "Lo"  # Formal pronouns
    ],
    "polite_expressions": [
        "Per favore", "Per cortesia", "Grazie", "Prego", 
        "Scusi", "Mi dispiace", "Certamente", "Naturalmente"
    ],
    "medical_courtesy": [
        "Come si sente?", "Ha dolore?", "Sta meglio?",
        "Non si preoccupi", "È normale", "Capisco"
    ]
}

# Training data for specific dental scenarios
SCENARIO_TRAINING_DATA = {
    "appointment_booking": {
        "keywords": ["appuntamento", "prenotare", "fissare", "disponibilità"],
        "responses": ["controllo la disponibilità", "che tipo di visita", "per quando"],
        "follow_up": ["nome", "telefono", "conferma"]
    },
    
    "emergency": {
        "keywords": ["dolore", "male", "emergenza", "urgente", "rotto"],
        "responses": ["mi dispiace", "capisco", "urgente", "subito"],
        "follow_up": ["descriva", "tipo di dolore", "quando è iniziato"]
    },
    
    "information": {
        "keywords": ["quanto costa", "prezzo", "assicurazione", "orari", "dove"],
        "responses": ["le fornisco", "controllo", "verifichiamo"],
        "follow_up": ["altro", "desidera prenotare", "altre domande"]
    }
}

def get_training_examples():
    """Return formatted training examples for the model"""
    return {
        "terminology": ITALIAN_DENTAL_TERMINOLOGY,
        "conversations": CONVERSATION_EXAMPLES,
        "prompts": TRAINING_PROMPTS,
        "scenarios": SCENARIO_TRAINING_DATA
    }
