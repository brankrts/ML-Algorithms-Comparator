
import matplotlib.pyplot as plt



class Compare:


    def __init__(self,provider):

        self.provider = provider
        self.params = self.provider.classify()
        self.model_names = [key for key in self.params]
        self.model_acc = [self.params[key] for key in self.model_names ]

    def compare(self):

        plt.figure(figsize=(10,5))
        plt.xticks(rotation=11)
        plt.plot(self.model_names , self.model_acc)
        plt.xlabel("Modeller")
        plt.ylabel("Dogruluk")
        plt.title('Mnist verisetinde model performanslari')

        plt.show()







