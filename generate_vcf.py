import sys

# Take arguments from workflow input
name = sys.argv[1]
org = sys.argv[2]
title = sys.argv[3]
phone = sys.argv[4]
email = sys.argv[5]
address = sys.argv[6]
website = sys.argv[7]

vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
ORG:{org}
TITLE:{title}
TEL;TYPE=WORK,VOICE:{phone}
EMAIL:{email}
ADR;TYPE=WORK:;;{address}
URL:{website}
END:VCARD
"""

with open("contact.vcf", "w") as f:
    f.write(vcf_content)

print("✅ VCF file generated: contact.vcf")
