from model_provider import ModelProvider
from compare import Compare

if __name__ == "__main__":

    provider = ModelProvider()
    compare = Compare(provider)
    compare.compare()
    
