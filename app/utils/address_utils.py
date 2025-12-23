def is_precise_address(location_data: dict) -> bool:
    """
    Returns True only if address is precise enough
    for property-level verification.
    """

    address = location_data.get("formatted_address", "").lower()

    precision_keywords = [
        "plot",
        "bungalow",
        "house",
        "villa",
        "flat",
        "apartment",
        "survey",
        "road",
        "lane",
        "society"
    ]

    return any(keyword in address for keyword in precision_keywords)
