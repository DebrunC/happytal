from pathlib import Path

class Settings:
	PROJECT_TITLE: str = "Recommender System"
	PROJECT_VERSION: str = "0.1.0"
	PACKAGE_ROOT: str = Path.cwd()
	SIMILARITY_MATRIX:str = PACKAGE_ROOT/"dataset/simMatrix.csv"
	USER_TO_PRODUCT: str = PACKAGE_ROOT/"dataset/userToProduct.csv"
	NUMBER_RECOMMENDATIONS :int = 5


settings = Settings()
