#!/usr/bin/env python3
"""
Simple test for the Italian Dental Clinic components without LiveKit dependencies
"""

import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_clinic_knowledge():
    """Test clinic knowledge base"""
    print("🏥 Testing Clinic Knowledge Base...")
    
    try:
        from clinic_knowledge import CLINIC_INFO, SERVICES, FAQ, APPOINTMENT_TYPES
        
        # Test clinic info structure
        assert "name" in CLINIC_INFO
        assert "address" in CLINIC_INFO
        assert "phone" in CLINIC_INFO
        assert "hours" in CLINIC_INFO
        
        print(f"✅ Clinic name: {CLINIC_INFO['name']}")
        print(f"✅ Address: {CLINIC_INFO['address']}")
        print(f"✅ Phone: {CLINIC_INFO['phone']}")
        
        # Test services
        assert len(SERVICES) > 0
        for service_key, service_data in SERVICES.items():
            assert "name" in service_data
            assert "description" in service_data
            assert "price_range" in service_data
        
        print(f"✅ Services loaded: {len(SERVICES)} services")
        
        # Test FAQ
        assert len(FAQ) > 0
        for faq_key, faq_data in FAQ.items():
            assert "question" in faq_data
            assert "answer" in faq_data
        
        print(f"✅ FAQ loaded: {len(FAQ)} questions")
        
        # Test appointment types
        assert len(APPOINTMENT_TYPES) > 0
        print(f"✅ Appointment types: {len(APPOINTMENT_TYPES)} types")
        
        print("✅ Clinic knowledge base test passed!\n")
        return True
        
    except Exception as e:
        print(f"❌ Clinic knowledge test failed: {e}")
        return False

def test_italian_training_data():
    """Test Italian training data"""
    print("🇮🇹 Testing Italian Training Data...")
    
    try:
        from italian_training_data import (
            ITALIAN_DENTAL_TERMINOLOGY, CONVERSATION_EXAMPLES, 
            TRAINING_PROMPTS, SCENARIO_TRAINING_DATA
        )
        
        # Test terminology
        assert len(ITALIAN_DENTAL_TERMINOLOGY) > 0
        print(f"✅ Dental terminology: {len(ITALIAN_DENTAL_TERMINOLOGY)} terms")
        
        # Test conversation examples
        assert len(CONVERSATION_EXAMPLES) > 0
        for example in CONVERSATION_EXAMPLES:
            assert "scenario" in example
            assert "conversation" in example
        print(f"✅ Conversation examples: {len(CONVERSATION_EXAMPLES)} scenarios")
        
        # Test training prompts
        assert len(TRAINING_PROMPTS) > 0
        print(f"✅ Training prompts: {len(TRAINING_PROMPTS)} prompts")
        
        # Test scenario data
        assert len(SCENARIO_TRAINING_DATA) > 0
        print(f"✅ Scenario data: {len(SCENARIO_TRAINING_DATA)} scenarios")
        
        print("✅ Italian training data test passed!\n")
        return True
        
    except Exception as e:
        print(f"❌ Italian training data test failed: {e}")
        return False

def test_conversation_flows():
    """Test Italian conversation flows"""
    print("💬 Testing Italian Conversation Flows...")
    
    try:
        from italian_conversation_flows import (
            GREETING_RESPONSES, APPOINTMENT_BOOKING_FLOWS,
            EMERGENCY_RESPONSES, SERVICE_INQUIRY_RESPONSES
        )
        
        # Test greetings
        assert len(GREETING_RESPONSES) > 0
        for greeting in GREETING_RESPONSES:
            assert "Sofia" in greeting or "Studio" in greeting
        print(f"✅ Greeting responses: {len(GREETING_RESPONSES)} greetings")
        
        # Test appointment flows
        assert "initial_request" in APPOINTMENT_BOOKING_FLOWS
        assert "confirming_appointment" in APPOINTMENT_BOOKING_FLOWS
        print("✅ Appointment booking flows loaded")
        
        # Test emergency responses
        assert len(EMERGENCY_RESPONSES) > 0
        print(f"✅ Emergency responses: {len(EMERGENCY_RESPONSES)} responses")
        
        # Test service inquiry responses
        assert "general_services" in SERVICE_INQUIRY_RESPONSES
        assert "pricing" in SERVICE_INQUIRY_RESPONSES
        print("✅ Service inquiry responses loaded")
        
        print("✅ Italian conversation flows test passed!\n")
        return True
        
    except Exception as e:
        print(f"❌ Conversation flows test failed: {e}")
        return False

def test_patient_database():
    """Test patient database functionality"""
    print("👤 Testing Patient Database...")
    
    try:
        from patient_database import PatientDatabase, AppointmentDatabase
        
        # Test patient database
        patient_db = PatientDatabase("test_patients.json")
        
        # Add test patient
        test_patient = {
            "name": "Mario Rossi",
            "phone": "+39 333 1234567",
            "email": "mario@test.com"
        }
        
        result = patient_db.add_patient(test_patient)
        assert "successo" in result
        print("✅ Patient added successfully")
        
        # Retrieve patient
        retrieved = patient_db.get_patient("+39 333 1234567")
        assert retrieved is not None
        assert retrieved["name"] == "Mario Rossi"
        print("✅ Patient retrieved successfully")
        
        # Test appointment database
        appointment_db = AppointmentDatabase("test_appointments.json")
        
        test_appointment = {
            "patient_name": "Mario Rossi",
            "phone": "+39 333 1234567",
            "date": "2024-01-15",
            "time": "10:00",
            "type": "visita_controllo"
        }
        
        app_id = appointment_db.add_appointment(test_appointment)
        assert app_id != ""
        print("✅ Appointment added successfully")
        
        # Check availability
        available = appointment_db.check_availability("2024-01-15", "10:00")
        assert not available  # Should be False since we just booked it
        print("✅ Availability check working")
        
        # Clean up test files
        import os
        try:
            os.remove("test_patients.json")
            os.remove("test_appointments.json")
        except:
            pass
        
        print("✅ Patient database test passed!\n")
        return True
        
    except Exception as e:
        print(f"❌ Patient database test failed: {e}")
        return False

def test_prompts():
    """Test Italian prompts"""
    print("📝 Testing Italian Prompts...")
    
    try:
        from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
        
        # Test agent instruction
        assert "Sofia" in AGENT_INSTRUCTION
        assert "Studio Dentistico" in AGENT_INSTRUCTION
        assert "italiano" in AGENT_INSTRUCTION
        print("✅ Agent instruction contains Italian elements")
        
        # Test session instruction
        assert "Sofia" in SESSION_INSTRUCTION
        assert "Dottoressa Emanuela" in SESSION_INSTRUCTION
        assert "Buongiorno" in SESSION_INSTRUCTION
        print("✅ Session instruction contains Italian elements")
        
        print("✅ Italian prompts test passed!\n")
        return True
        
    except Exception as e:
        print(f"❌ Prompts test failed: {e}")
        return False

def test_italian_language_quality():
    """Test Italian language quality"""
    print("🇮🇹 Testing Italian Language Quality...")
    
    try:
        from clinic_knowledge import CLINIC_INFO, SERVICES
        
        # Check clinic name is in Italian
        clinic_name = CLINIC_INFO["name"]
        assert "Dottoressa" in clinic_name
        print("✅ Clinic name is in Italian")
        
        # Check services descriptions contain Italian
        italian_found = False
        for service_key, service_data in SERVICES.items():
            description = service_data["description"]
            if any(word in description.lower() for word in ["dentale", "orale", "denti", "visita"]):
                italian_found = True
                break
        
        assert italian_found
        print("✅ Services contain Italian terminology")
        
        print("✅ Italian language quality test passed!\n")
        return True
        
    except Exception as e:
        print(f"❌ Italian language quality test failed: {e}")
        return False

def run_all_tests():
    """Run all simple tests"""
    print("🚀 Starting Simple Italian Dental Clinic Tests...\n")
    
    tests = [
        test_clinic_knowledge,
        test_italian_training_data,
        test_conversation_flows,
        test_patient_database,
        test_prompts,
        test_italian_language_quality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The Italian Dental Clinic system is working correctly!")
        print("\n📋 Components Verified:")
        print("✅ Clinic knowledge base")
        print("✅ Italian training data")
        print("✅ Conversation flows")
        print("✅ Patient database")
        print("✅ Italian prompts")
        print("✅ Language quality")
        print("\n🇮🇹 Ready to deploy the Italian Dental Receptionist!")
        return True
    else:
        print(f"❌ {total - passed} tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
