import re

# Define the OpenAPI schema
receipt_schema = {
    "retailer": {"type": "string", "pattern": ".*"}, # Correction of Incorrect Regex "^\\S+$" from the task (not worked for Example "retailer": "M&M Corner Market") 
    "purchaseDate": {"type": "string", "format": "date"},
    "purchaseTime": {"type": "string", "format": "time"},
    "items": {"type": "array", "minItems": 1,
    "items": {"type": "object", "required": ["shortDescription", "price"],
        "properties": {"shortDescription":
                        {"type": "string","pattern": "^[\\w\\s\\-]+$"},
        "price": {"type": "string", "pattern": "^\\d+\\.\\d{2}$"}
            }
        }
    },
    "total": {"type": "string", "pattern": "^\\d+\\.\\d{2}$"},
}

# Validate receipt
def validate_receipt(receipt):
    for field, schema in receipt_schema.items():
        if field not in receipt:
            raise Exception(f"Field '{field}' is missing.")
        value = receipt[field]
        if schema.get("type") == "string" and schema.get("pattern") and not re.match(schema["pattern"], value):
            raise Exception(f"Invalid value for '{field}': {value}")
        if schema.get("type") == "array" and schema.get("minItems") and len(value) < schema["minItems"]:
            raise Exception(f"'{field}' must contain at least {schema['minItems']} items.")
