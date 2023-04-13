import pandas as pd
import tensorflow as tf
import chardet
from sklearn.preprocessing import StandardScaler

def train_model():
    cols = ["OID_"," id", "floor_area_sf", "civic_number"]
    ### FOR TRAINING WITH MULTIPLE FILES ###
    ### CHANGE THE FILE PATHS TO THE PATHS OF THE FILES YOU WANT TO TRAIN WITH ###
    ### MAKE SURE TO USE THE ABSOLUTE PATHS !!! ###

    # file_paths = ['./scripts/data/new_training1.csv', './scripts/data/new_training2.csv', './scripts/data/new_training3.csv']
    # train_data = ''
    # for file in file_paths:
    #     enc = chardet.detect(open(file, 'rb').read())
    #     data = pd.read_csv(file, encoding=enc['encoding'], usecols=cols)
    #     if train_data == '':
    #         train_data = data
    #     else:
    #         train_data = pd.concat([train_data, data])

    ### FOR TRAINING WITH ONE FILE ###
    ### IF USING THE ABOVE METHOD COMMENT OUT THE FOLLOWING CODE ###
    ### FROM HERE ###
    file_path = './scripts/data/new_training4.csv'
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
    
    with open(file_path, 'rb') as f:
        enc = chardet.detect(f.read())
    
    train_data = pd.read_csv(file_path, encoding=enc['encoding'], usecols=cols)
    ### TO HERE ###

    X_train = train_data.drop(['floor_area_sf'], axis=1)
    y_train = train_data['floor_area_sf']
    
    scaler = StandardScaler()
    cols.remove("floor_area_sf")
    X_train[cols] = scaler.fit_transform(X_train[cols])
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=[X_train.shape[1]]),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    
    model.compile(optimizer=optimizer, loss='mae', metrics=['mean_squared_error'])
    weight_path = './scripts/data/model_weights.h5'
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)
    best_saves = tf.keras.callbacks.ModelCheckpoint(weight_path, monitor='loss', save_best_only=True)
    
    tf.random.set_seed(42)
    if X_train.shape[0] < 200:
        epochs = 10
    else:
        epochs = 5
    
    for i in range(1):
        model.load_weights(weight_path)
        model.fit(X_train, y_train, epochs=1, callbacks=[best_saves,early_stopping])
    
  
    return model


def predict(model, test_data):
    cols2 = ["OID_"," id", "floor_area_sf", "civic_number"]
    
    for col in test_data.columns.values:
        if "id" in col:
            if col == "id":
                ind = cols2.index(" id")
                cols2[ind] = col
    
    ### IF TEST DATA HAS NO MISSING VALUES THEN RETURN IT ###
    is_missing_vals = test_data['floor_area_sf'].isna().any()
    if not is_missing_vals:
        return test_data
    
    ### IF TEST DATA HAS MISSING VALUES THEN BEGIN USE ONLY NA VALUES ###
    test_data = test_data[test_data['floor_area_sf'].isna()]
    result = test_data
    test_data = test_data[cols2]
    
    scaler = StandardScaler()
    cols2.remove("floor_area_sf")

    ### DATA CLEANING ###
    ### CHECK IF COLUMN IS NUMERIC THEN CONVERT IT TO NUMERIC ###
    ### IF NOT THEN FILL THE MISSING VALUES WITH THE MEAN OF THE COLUMN ###
    for col in test_data.columns:
        if pd.to_numeric(test_data[col], errors='coerce').notnull().all():
            test_data[col] = pd.to_numeric(test_data[col])    
        else:
            col_mean = pd.to_numeric(test_data[col], errors='coerce', downcast='float').mean(skipna=True)
            test_data[col] = pd.to_numeric(test_data[col], errors='coerce', downcast='float')
            test_data[col].fillna(value=col_mean, inplace=True)

    scaler.fit(test_data[cols2])
    test_data[cols2] = scaler.transform(test_data[cols2])
    weight_path = './scripts/data/model_weights.h5'

    model.load_weights(weight_path)
    predictions = model.predict(test_data.drop(['floor_area_sf'], axis=1))
    result['floor_area_sf_predicted'] = predictions.reshape(-1)
    
    result.drop(['floor_area_sf'], axis=1, inplace=True)
    return result
