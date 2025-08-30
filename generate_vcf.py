import os

# Example multiple contacts
contacts = [
    {
        "FN": "John Doe",
        "ORG": "Noweapon Digitals Consult",
        "TITLE": "Digital Consultant",
        "TEL": "+233123456789",
        "EMAIL": "johndoe@example.com",
        "ADR": "Accra;Greater Accra;;Ghana",
        "URL": "https://noweapondigitals.com"
    },
    {
        "FN": "Mary Smith",
        "ORG": "Noweapon Digitals Consult",
        "TITLE": "Project Manager",
        "TEL": "+233987654321",
        "EMAIL": "marysmith@example.com",
        "ADR": "Kumasi;Ashanti;;Ghana",
        "URL": "https://noweapondigitals.com/team"
    }
]

# Generate VCF file
def create_vcf(contacts, filename="contacts.vcf"):
    with open(filename, "w", encoding="utf-8") as f:
        for contact in contacts:
            f.write("BEGIN:VCARD\n")
            f.write("VERSION:3.0\n")
            f.write(f"FN:{contact['FN']}\n")
            f.write(f"ORG:{contact['ORG']}\n")
            f.write(f"TITLE:{contact['TITLE']}\n")
            f.write(f"TEL;TYPE=WORK,VOICE:{contact['TEL']}\n")
            f.write(f"EMAIL:{contact['EMAIL']}\n")
            f.write(f"ADR;TYPE=WORK:;;{contact['ADR']}\n")
            f.write(f"URL:{contact['URL']}\n")
            f.write("END:VCARD\n")

create_vcf(contacts)
print("✅ contacts.vcf file generated successfully!")
