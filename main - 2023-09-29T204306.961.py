import random

# Simulated data sources (replace with real data sources)
buyer_leads = [
    {"name": "L", "zip_code": "90210"},
    {"name": "Buyer 2", "zip_code": "90210"},
    {"name": "Buyer 3", "zip_code": "94110"},
]

seller_leads = [
    {"name": "Seller 1", "zip_code": "90210"},
    {"name": "Seller 2", "zip_code": "94110"},
    {"name": "Seller 3", "zip_code": "90210"},
]

# Simulated CRM system (replace with a real CRM system integration)
crm_system = []

# Simulate CRM data with some random leads
for i in range(10):
    lead = random.choice(buyer_leads + seller_leads)
    crm_system.append(lead)

# Define the desired zip code
desired_zip_code = "90210"

# Filter leads based on the desired zip code
filtered_leads = [lead for lead in crm_system if lead.get("zip_code") == desired_zip_code]

# Generate a report
print(f"Leads in Zip Code {desired_zip_code}:")
for lead in filtered_leads:
    print(f"Name: {lead['name']}, Zip Code: {lead['zip_code']}")

