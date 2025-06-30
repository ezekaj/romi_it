#!/usr/bin/env python3
"""
Test script for the Italian Dental Clinic Receptionist Agent
Tests all major functionality and validates Italian language responses
"""

import asyncio
import sys
import os
from datetime import datetime, timedelta

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from dental_tools import (
        get_clinic_info, get_services_info, answer_faq,
        check_availability, schedule_appointment, collect_patient_info,
        cancel_appointment, reschedule_appointment,
        get_insurance_info, get_payment_info
    )
    from clinic_knowledge import CLINIC_INFO, SERVICES, FAQ
    from italian_training_data import CONVERSATION_EXAMPLES
except ImportError as e:
    print(f"Import error: {e}")
    print("Some modules may not be available. Running basic tests only.")

class MockRunContext:
    """Mock RunContext for testing"""
    pass

async def test_clinic_info():
    """Test clinic information retrieval"""
    print("🏥 Testing Clinic Information...")
    context = MockRunContext()
    
    # Test general info
    result = await get_clinic_info(context, "general")
    print(f"General Info: {result[:100]}...")
    assert "Studio Dentistico Dottoressa Emanuela" in result
    
    # Test hours
    result = await get_clinic_info(context, "hours")
    print(f"Hours: {result[:100]}...")
    assert "lunedi" in result.lower() or "orari" in result.lower()
    
    # Test contact
    result = await get_clinic_info(context, "contact")
    print(f"Contact: {result[:100]}...")
    assert "+39" in result
    
    print("✅ Clinic info tests passed!\n")

async def test_services_info():
    """Test services information"""
    print("🦷 Testing Services Information...")
    context = MockRunContext()
    
    # Test all services
    result = await get_services_info(context, "all")
    print(f"All Services: {result[:100]}...")
    assert "Odontoiatria Generale" in result
    
    # Test specific service
    result = await get_services_info(context, "igiene_dentale")
    print(f"Dental Hygiene: {result[:100]}...")
    assert "Igiene Dentale" in result
    assert "€" in result
    
    print("✅ Services info tests passed!\n")

async def test_faq():
    """Test FAQ functionality"""
    print("❓ Testing FAQ...")
    context = MockRunContext()
    
    result = await answer_faq(context, "costi")
    print(f"FAQ Costs: {result[:100]}...")
    assert "costa" in result.lower()
    
    result = await answer_faq(context, "assicurazioni")
    print(f"FAQ Insurance: {result[:100]}...")
    assert "assicuraz" in result.lower()
    
    print("✅ FAQ tests passed!\n")

async def test_availability():
    """Test availability checking"""
    print("📅 Testing Availability...")
    context = MockRunContext()
    
    # Test future date
    future_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    result = await check_availability(context, future_date, "visita_controllo")
    print(f"Future availability: {result[:100]}...")
    assert "Disponibilità" in result or "disponibilità" in result
    
    # Test past date
    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    result = await check_availability(context, past_date, "visita_controllo")
    print(f"Past date: {result[:100]}...")
    assert "passate" in result
    
    print("✅ Availability tests passed!\n")

async def test_appointment_booking():
    """Test appointment booking"""
    print("📝 Testing Appointment Booking...")
    context = MockRunContext()
    
    future_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
    result = await schedule_appointment(
        context,
        patient_name="Mario Rossi",
        phone="+39 333 1234567",
        date=future_date,
        time="10:00",
        appointment_type="visita_controllo",
        notes="Prima visita"
    )
    print(f"Booking result: {result[:100]}...")
    assert "confermato" in result
    assert "Mario Rossi" in result
    
    print("✅ Appointment booking tests passed!\n")

async def test_patient_info_collection():
    """Test patient information collection"""
    print("👤 Testing Patient Info Collection...")
    context = MockRunContext()
    
    result = await collect_patient_info(
        context,
        name="Giulia Bianchi",
        phone="+39 333 7654321",
        email="giulia@email.com",
        birth_date="1985-03-15",
        medical_conditions="Nessuna",
        medications="Nessuno",
        allergies="Penicillina",
        previous_dentist="Dr. Verdi"
    )
    print(f"Patient info: {result[:100]}...")
    assert "Giulia Bianchi" in result
    assert "registrate" in result
    
    print("✅ Patient info tests passed!\n")

async def test_cancellation():
    """Test appointment cancellation"""
    print("❌ Testing Appointment Cancellation...")
    context = MockRunContext()
    
    # First book an appointment to cancel
    future_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    await schedule_appointment(
        context,
        patient_name="Test Patient",
        phone="+39 333 9999999",
        date=future_date,
        time="14:00",
        appointment_type="visita_controllo"
    )
    
    # Now cancel it
    result = await cancel_appointment(
        context,
        patient_name="Test Patient",
        phone="+39 333 9999999",
        date=future_date,
        time="14:00"
    )
    print(f"Cancellation: {result[:100]}...")
    assert "cancellato" in result
    
    print("✅ Cancellation tests passed!\n")

async def test_insurance_info():
    """Test insurance information"""
    print("🏥 Testing Insurance Info...")
    context = MockRunContext()
    
    # Test specific insurance
    result = await get_insurance_info(context, "Unisalute")
    print(f"Unisalute info: {result[:100]}...")
    assert "Unisalute" in result
    
    # Test all insurances
    result = await get_insurance_info(context, "")
    print(f"All insurances: {result[:100]}...")
    assert "Generali" in result
    
    print("✅ Insurance info tests passed!\n")

async def test_payment_info():
    """Test payment information"""
    print("💳 Testing Payment Info...")
    context = MockRunContext()
    
    result = await get_payment_info(context)
    print(f"Payment info: {result[:100]}...")
    assert "pagamento" in result
    assert "carte" in result.lower()
    
    print("✅ Payment info tests passed!\n")

def test_italian_language_quality():
    """Test Italian language quality in responses"""
    print("🇮🇹 Testing Italian Language Quality...")
    
    # Check if key Italian phrases are present in knowledge base
    italian_phrases = [
        "Buongiorno", "appuntamento", "visita", "dottoressa",
        "disponibilità", "prenotazione", "emergenza", "dolore"
    ]
    
    # Test clinic info contains Italian
    clinic_name = CLINIC_INFO["name"]
    assert "Dottoressa" in clinic_name
    
    # Test services are in Italian
    for service_key, service_data in SERVICES.items():
        assert any(char in "àèéìíîòóù" for char in service_data["description"].lower()) or \
               any(word in service_data["description"] for word in ["dentale", "orale", "estetica"])
    
    print("✅ Italian language quality tests passed!\n")

def test_conversation_examples():
    """Test conversation examples structure"""
    print("💬 Testing Conversation Examples...")
    
    for example in CONVERSATION_EXAMPLES:
        assert "scenario" in example
        assert "conversation" in example
        assert len(example["conversation"]) > 0
        
        for turn in example["conversation"]:
            assert "speaker" in turn
            assert "text" in turn
            assert turn["speaker"] in ["paziente", "sofia"]
    
    print("✅ Conversation examples tests passed!\n")

async def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Italian Dental Clinic Agent Tests...\n")
    
    try:
        await test_clinic_info()
        await test_services_info()
        await test_faq()
        await test_availability()
        await test_appointment_booking()
        await test_patient_info_collection()
        await test_cancellation()
        await test_insurance_info()
        await test_payment_info()
        test_italian_language_quality()
        test_conversation_examples()
        
        print("🎉 All tests passed successfully!")
        print("\n📋 Test Summary:")
        print("✅ Clinic information retrieval")
        print("✅ Services information")
        print("✅ FAQ responses")
        print("✅ Availability checking")
        print("✅ Appointment booking")
        print("✅ Patient information collection")
        print("✅ Appointment cancellation")
        print("✅ Insurance information")
        print("✅ Payment information")
        print("✅ Italian language quality")
        print("✅ Conversation examples")
        
        print("\n🇮🇹 The Italian Dental Clinic Receptionist Agent is ready!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)
