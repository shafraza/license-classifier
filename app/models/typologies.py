from enum import Enum

class Typology(str, Enum):
    PRODUCTIVITY = "Productivity"
    DESIGN = "Design"
    COMMUNICATION = "Communication"
    DEVELOPMENT = "Development"
    FINANCE = "Finance"
    MARKETING = "Marketing"

TYPING_CATEGORIES = [
    Typology.PRODUCTIVITY,
    Typology.DESIGN,
    Typology.COMMUNICATION,
    Typology.DEVELOPMENT,
    Typology.FINANCE,
    Typology.MARKETING,
]
