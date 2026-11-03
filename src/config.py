from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SEED = 42

# Chemins 

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Ce fichier sera créé après l'inventaire des patients.
PATIENTS_CSV = DATA_DIR / "patients.csv"

REPORTS_DIR = PROJECT_ROOT / "reports"
EDA_DIR = REPORTS_DIR / "eda"
FIGURES_DIR = EDA_DIR / "figures"


# Données 

MODALITY = "MRI_T2"

EXPECTED_DEVELOPMENT_PATIENTS = 8
EXPECTED_TEST_PATIENTS = 4

# Les patients de test restent séparés pendant le développement.
INCLUDE_TEST_IN_EDA = False
