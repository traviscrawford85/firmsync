from firm_documents.models.pip_letter_of_representation import PipLetterOfRepresentation

test_data = {
    "matter": {
        "client_name": "Johnathan Mitchell",
        "custom": {
            "date_of_loss": "2024-10-12",
            "claim_number": "CLM-123456",
            "policy_number": "POL-654321",
            "user_initials": "JM"
        }
    },
    "insurance": {
        "adjuster_full_name": "Sarah Adjuster",
        "adjuster_email": "sarah.adjuster@insuranceco.com",
        "insurance_name": "Liberty Insurance",
        "insurance_address": "123 Liberty Ave, New York, NY 10001"
    },
    "firm": {
        "attorney": "Attorney Smith"
    }
}

doc_model = PipLetterOfRepresentation(**test_data)
