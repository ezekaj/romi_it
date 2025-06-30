# 🦷 Studio Dentistico Emanuela - AI Receptionist Setup Guide

## Overview
This guide will help you set up the Italian-speaking AI receptionist for Emanuela's Dental Clinic. The agent is built on LiveKit with Google's Realtime Model and is specifically designed for dental clinic reception tasks in Italian.

## 🎯 Features Implemented

### Core Functionality
- ✅ **Appointment Management**: Scheduling, rescheduling, cancellation
- ✅ **Italian Language Support**: Native Italian conversation flows
- ✅ **Dental Services Information**: Complete service catalog with pricing
- ✅ **Patient Information Collection**: Contact details and medical history
- ✅ **Insurance Handling**: Coverage verification and billing information
- ✅ **Emergency Prioritization**: Urgent appointment scheduling
- ✅ **FAQ Responses**: Common dental clinic questions

### Language Features
- ✅ **Italian Dental Terminology**: Comprehensive medical vocabulary
- ✅ **Natural Conversation Flows**: Receptionist-style interactions
- ✅ **Formal Italian Address**: Proper "Lei" form usage
- ✅ **Empathetic Responses**: Pain and anxiety acknowledgment

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Activate the virtual environment
cd "c:\Users\User\OneDrive\Desktop\elo_base - Copy"
.\elvi_env\Scripts\activate

# Install any missing dependencies
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file with your API keys:
```env
# Google API Configuration
GOOGLE_API_KEY=your_google_api_key_here

# LiveKit Configuration  
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Optional: Email configuration for appointment confirmations
GMAIL_USER=your_gmail@gmail.com
GMAIL_APP_PASSWORD=your_app_password
```

### 3. Test the Agent
```bash
# Run the test suite
python test_dental_agent.py

# Start the agent
python agent.py
```

## 📋 File Structure

```
elo_base - Copy/
├── agent.py                    # Main agent configuration (updated for Italian)
├── prompts.py                  # Italian prompts and instructions
├── dental_tools.py             # Dental clinic specific tools
├── clinic_knowledge.py         # Clinic information database
├── patient_database.py         # Patient and appointment management
├── italian_conversation_flows.py # Italian conversation patterns
├── italian_training_data.py    # Training data and terminology
├── test_dental_agent.py        # Comprehensive test suite
└── DENTAL_CLINIC_SETUP.md      # This setup guide
```

## 🔧 Configuration Details

### Agent Configuration (agent.py)
- **Model**: Google Realtime Model with Italian language support
- **Voice**: "Puck" (suitable for Italian)
- **Language**: "it-IT" (Italian)
- **Temperature**: 0.7 (balanced creativity/consistency)

### Clinic Information (clinic_knowledge.py)
Update the following sections with your actual clinic details:

```python
CLINIC_INFO = {
    "name": "Studio Dentistico Dottoressa Emanuela",
    "address": "Your actual address",
    "phone": "Your phone number",
    "email": "Your email",
    # ... update all fields
}
```

### Services and Pricing
Customize the services and pricing in `clinic_knowledge.py`:
```python
SERVICES = {
    "igiene_dentale": {
        "price_range": "€80-120"  # Update with your prices
    },
    # ... update all services
}
```

## 🧪 Testing

### Run Comprehensive Tests
```bash
python test_dental_agent.py
```

### Manual Testing Scenarios
1. **Appointment Booking**: "Vorrei fissare un appuntamento"
2. **Emergency**: "Ho un forte mal di denti"
3. **Service Inquiry**: "Quanto costa una pulizia?"
4. **Insurance**: "Accettate Unisalute?"
5. **Cancellation**: "Devo cancellare l'appuntamento"

## 🎭 Italian Language Features

### Conversation Starters
- "Buongiorno, sono Sofia, l'assistente virtuale dello Studio Dentistico della Dottoressa Emanuela"
- "Come posso aiutarla oggi?"
- "In cosa posso esserle utile?"

### Common Responses
- **Appointment**: "Controllo subito la disponibilità"
- **Emergency**: "Capisco il suo dolore, cerchiamo di trovarle posto subito"
- **Information**: "Le fornisco subito le informazioni"

### Dental Terminology
- Appuntamento (appointment)
- Visita di controllo (check-up)
- Pulizia dei denti (dental cleaning)
- Emergenza dentale (dental emergency)
- Mal di denti (toothache)

## 🔄 Customization

### Adding New Services
1. Update `SERVICES` in `clinic_knowledge.py`
2. Add to `APPOINTMENT_TYPES` if bookable
3. Update FAQ if needed

### Modifying Conversation Flows
1. Edit `italian_conversation_flows.py`
2. Update prompts in `prompts.py`
3. Test with new scenarios

### Database Integration
Replace the simple JSON storage in `patient_database.py` with:
- PostgreSQL for production
- Integration with existing practice management software
- GDPR-compliant patient data handling

## 📞 LiveKit Integration

### Voice Configuration
The agent uses Google's Realtime Model with:
- **Voice**: "Puck" (clear Italian pronunciation)
- **Language**: "it-IT"
- **Noise Cancellation**: BVC for clear audio

### Room Setup
```python
room_input_options=RoomInputOptions(
    video_enabled=True,
    noise_cancellation=noise_cancellation.BVC(),
)
```

## 🔐 Security Considerations

### Patient Data Protection
- Implement GDPR compliance
- Encrypt sensitive patient information
- Use secure database connections
- Regular data backups

### API Security
- Store API keys in environment variables
- Use HTTPS for all communications
- Implement rate limiting
- Monitor for unusual activity

## 📈 Monitoring and Analytics

### Key Metrics to Track
- Appointment booking success rate
- Average conversation length
- Common patient inquiries
- Emergency response time
- Patient satisfaction

### Logging
The agent logs important events:
- Appointment bookings
- Cancellations
- Error conditions
- Patient interactions

## 🚨 Troubleshooting

### Common Issues

1. **Italian Language Not Working**
   - Verify `language="it-IT"` in agent.py
   - Check Google API supports Italian
   - Ensure prompts are in Italian

2. **Appointment Booking Fails**
   - Check date format (YYYY-MM-DD)
   - Verify time format (HH:MM)
   - Ensure database permissions

3. **Voice Quality Issues**
   - Check LiveKit configuration
   - Verify noise cancellation settings
   - Test microphone/speaker setup

### Debug Mode
Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Support

For technical support:
- Check the test results: `python test_dental_agent.py`
- Review logs for error messages
- Verify all API keys are correctly configured
- Ensure all dependencies are installed

## 🎉 Go Live Checklist

- [ ] All tests pass
- [ ] Clinic information updated
- [ ] Services and pricing configured
- [ ] Insurance list updated
- [ ] Staff trained on system
- [ ] Backup procedures in place
- [ ] Monitoring configured
- [ ] Patient privacy compliance verified

The Italian Dental Clinic Receptionist Agent is now ready to serve Emanuela's patients! 🇮🇹🦷
