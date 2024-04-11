from sklearn import svm, tree
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from WaterClassifier.graphics import imprimeGraficos


def classificaDados(dados, classes_metodos,classes_qualidade_agua):

    ####### INICIO DO PROCESSO DE CLASSIFICACAO: DADOS E TARGETS 
    #1° passo: retirar labels para alocar em y e retirar infos desnecessárias

    x = dados.drop(['STATION CODE', 'LOCATIONS', 'STATE', 'Temp', 'WQI', 'classe', 'year'], axis=1)
    y = dados['classe']

    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)

    #2° PASSO: aplicar modelos

    valor_test = 0.4

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= valor_test, random_state=1)

    ##KNN 

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train,y_train)
    y_pred_knn = knn.predict(x_test)
    #print(confusion_matrix(y_test,y_pred_knn))

    #SVM

    clf = svm.SVC(kernel='linear').fit(x_train,y_train)
    y_pred_svm = clf.predict(x_test)
    #print(confusion_matrix(y_test,y_pred_svm))

    #MLP

    classifier = MLPClassifier()
    classifier.fit(x_train,y_train)
    y_pred_mlp = classifier.predict(x_test)
    #print(confusion_matrix(y_test,y_pred_mlp))

    #ARVORE DE DECISAO

    tree_classifier = tree.DecisionTreeClassifier()
    tree_classifier = tree_classifier.fit(x_train,y_train)
    y_pred_tree = tree_classifier.predict(x_test)
    #print(confusion_matrix(y_test,y_pred_tree))

    #NAIVE BAYES

    gnb_classifier = GaussianNB()
    gnb_classifier = gnb_classifier.fit(x_train,y_train)
    y_pred_nb = gnb_classifier.predict(x_test)
    #print(confusion_matrix(y_test,y_pred_nb))

    #matrizes de confusao geradas

    knn_dados = confusion_matrix(y_test,y_pred_knn)
    svm_dados = confusion_matrix(y_test,y_pred_svm)
    mlp_dados = confusion_matrix(y_test,y_pred_mlp)
    tree_dados = confusion_matrix(y_test,y_pred_tree)
    gnb_dados = confusion_matrix(y_test,y_pred_nb)

    ####comparacao final com graficos de confusao

    arrays_confusao = [knn_dados,svm_dados,mlp_dados,tree_dados,gnb_dados]

    imprimeGraficos(arrays_confusao,classes_metodos,classes_qualidade_agua)