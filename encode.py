import pdf417gen
from PIL import Image

def hub3_field(text, max_length):
    """Ensure field does not exceed the max length (truncation only)."""
    return text if len(text) <= max_length else text[:max_length]

# --- HUB3 fields ---

# 1. Header – fixed value
header = "HRVHUB30"  # exactly 8 characters

# 2. Currency – using EUR for this example
currency = "EUR"     # 3 characters

# 3. Amount – for 40,00€; value in cents (40€ = 4000 cents) padded to 15 digits
amount = f"{4000:015d}"  # yields "000000000004000"

# 4. Payer Name – from your provided info
payer_name = hub3_field("Lovro Krčelić", 30)

# 5. Payer Address – not provided (empty)
payer_address = ""

# 6. Payer Postal Code and City – not provided (empty)
payer_city = ""

# 7. Recipient Name – not specified; use a placeholder (or replace with actual name)
recipient_name = hub3_field("TEMPLAR ZAGREB", 25)

# 8. Recipient Address – not provided (empty)
recipient_address = ""

# 9. Recipient Postal Code and City – not provided (empty)
recipient_city = ""

# 10. IBAN – from your provided info
iban = "HR6224020061101201791"  # must be 21 characters

# 11. Model – typically a 4-character code; using "HR00" as a default
model = "HR00"

# 12. Reference – the “Poziv na broj”; here a short placeholder version is used
reference = hub3_field("02-2024", 22)

# 13. Purpose Code – for example, "COST" for cost/payment purpose
purpose_code = ""

# 14. Payment Description – from your provided info
description = hub3_field("Članarina za 02-2024", 35)

# Assemble all fields separated by LF (line feed) with a trailing LF.
fields = [
    header,
    currency,
    amount,
    payer_name,
    payer_address,
    payer_city,
    recipient_name,
    recipient_address,
    recipient_city,
    iban,
    model,
    reference,
    purpose_code,
    description,
]

data = "\n".join(fields) + "\n"

# --- Generate PDF417 barcode ---
# The HUB3 specification requires 9 data columns and error correction level 4.
codes = pdf417gen.encode(data, columns=9, security_level=4)
barcode_img = pdf417gen.render_image(codes, scale=3, ratio=3, padding=5)

# Save the barcode image.
barcode_img.save("hub3_payment_barcode.png")
print("Barcode saved to hub3_payment_barcode.png")
