import pickle

def run_model(model_choice, costs_choice, col_values):
    if(model_choice == 'Repair Cost'):
        if(costs_choice == 'With Cost'):
            with open('modelwithamounts_rc.pkl', 'rb') as f:
                model = pickle.load(f)
                X = []
                X.append(list(col_values.values()))
                prediction = model.predict(X)[0]
                return prediction
        else:
            with open('modelwithoutamounts_rc.pkl', 'rb') as f:
                model = pickle.load(f)
                X = []
                X.append(list(col_values.values()))
                prediction = model.predict(X)[0]
                return prediction
    else:
        if (costs_choice == 'With Cost'):
            with open('modelwithamounts_pmc.pkl', 'rb') as f:
                model = pickle.load(f)
                X = []
                X.append(list(col_values.values()))
                prediction = model.predict(X)[0]
                return prediction
        else:
            with open('modelwithoutamounts_pmc.pkl', 'rb') as f:
                model = pickle.load(f)
                X = []
                X.append(list(col_values.values()))
                prediction = model.predict(X)[0]
                return prediction
