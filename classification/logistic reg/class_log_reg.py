class Logistic_Regression():  # class-> template/blueprint of each obj(classifier)
    
    def __init__(self,learning_rate=0.01,no_of_iterations=1000):  # default values given - can change values while creating obj
        self.learning_rate = learning_rate        
        self.no_of_iterations = no_of_iterations
    
    def fit(self,x,y):  # fitting obj with x and y given arrays
        self.m,self.n=X.shape
        self.w = np.zeroes(self.n) # intialize wight array for each feature
        self.b = 0  # intializing bias as 0
        self.x = x 
        self.y = y
        
        # gradient descent ->
        for i in range (no_of_iterations) :
            self.update_weight()
        
    def update_weight(self):
        
        Y_sigmoid = 1/(1+np.exp(-(self.x.dot(self.w)+self.b)))  
        
        #slopes :
        dw = (1/self.m)*np.dot(self.x.T,(Y_sigmoid-self.y))
        db = (1/self.m)*np.sum(Y_sigmoid-self.y)
        
        # updating :
        self.w = self.w - self.learning_rate*dw
        self.b = self.b - self.learning_rate*db
        
        
    def predict(self):
        y_pred = 1/(1+np.exp(-(self.x.dot(self.w)+self.b)))
        y_pred = np.where(y_pred>0.5 , 1,0)  # 0.5 -> decision boundary
        return y_pred