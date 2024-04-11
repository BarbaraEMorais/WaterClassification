import seaborn as sns
import matplotlib.pyplot as plt

def imprimeGraficos(arrays_confusao,classes_metodos,classes_qualidade_agua):

    for i in range(len(arrays_confusao)):
        sns.heatmap(arrays_confusao[i], cmap='coolwarm', annot=True, linewidth=1, fmt='d')
        plt.title(classes_metodos[i])
        plt.show()


    #conjunto de tabelas comparativas
    def plot_confusion_matrix(ax, cm, title):
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels= classes_qualidade_agua, yticklabels= classes_qualidade_agua, ax=ax)
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_title(title)


    fig, axes = plt.subplots(1, 5, figsize=(20, 4))

    plot_confusion_matrix(axes[0], arrays_confusao[0], title= classes_metodos[0])
    plot_confusion_matrix(axes[1], arrays_confusao[1], title= classes_metodos[1])
    plot_confusion_matrix(axes[2], arrays_confusao[2], title= classes_metodos[2])
    plot_confusion_matrix(axes[3], arrays_confusao[3], title= classes_metodos[3])
    plot_confusion_matrix(axes[4], arrays_confusao[4], title= classes_metodos[4])

    plt.tight_layout()
    plt.show()
