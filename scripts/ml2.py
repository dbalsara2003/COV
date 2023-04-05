import tensorflow as tf
import pandas as pd
import numpy as np
import chardet

## OPTIMIZERS
# optimizer = tf.keras.optimizers.SGD(learning_rate=0.001) ///
# optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001) ///
# optimizer = tf.keras.optimizers.Adagrad(learning_rate=0.001)
# optimizer = tf.keras.optimizers.Adadelta(learning_rate=0.001)
# optimizer = tf.keras.optimizers.Adamax(learning_rate=0.001)
# optimizer = tf.keras.optimizers.Nadam(learning_rate=0.001)
# optimizer = tf.keras.optimizers.Ftrl(learning_rate=0.001)
# optimizer = tf.keras.optimizers.Optimizer(learning_rate=0.001)

def machine_learning(test_data: pd.DataFrame):
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

    # TRAINING DATA
    # file = './data/new_training4.csv'
    file = './scripts/data/new_training4.csv'
    # file2 = './data/new_training2.csv'
    # TEST DATA
    # file3 = './data/testing.csv'

    with open(file, 'rb') as f:
        enc = chardet.detect(f.read())

    # with open(file2, 'rb') as f:
    #     enc2 = chardet.detect(f.read())

    # with open(file3, 'rb') as f:
    #     enc3 = chardet.detect(f.read())

    cols = ["OID_"," id", "floor_area_sf", "civic_number"]



    test_data = test_data[test_data['floor_area_sf'].isna()]
    result = test_data
    test_data = test_data[cols]
    # Load training data
    train_data = pd.read_csv(file, encoding=enc['encoding'], usecols=cols)
    # data2 = pd.read_csv(file2, encoding=enc2['encoding'], usecols=cols)

    # train_data = pd.concat([data], ignore_index=True)
    # Preprocess data
    X_train = train_data.drop(['floor_area_sf'], axis=1)
    y_train = train_data['floor_area_sf']

    X_train = X_train.astype(np.float32)
    y_train = y_train.astype(np.float32)

    # Build model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='sigmoid', input_shape=[X_train.shape[1]]),
        tf.keras.layers.Dense(16, activation='sigmoid'),
        tf.keras.layers.Dense(1)
    ])

    # Compile model
    model.compile(optimizer=optimizer, loss='mae')

    # Train model 500 512 100
    model.fit(X_train, y_train, epochs=1, batch_size=1, steps_per_epoch=1)

    # Load test data
    # test_data = pd.read_csv(file3, encoding=enc3['encoding'], usecols=cols)

    # Preprocess test data
    X_test = test_data.drop(['floor_area_sf'], axis=1)
    X_test = X_test.astype(np.float32)

    # Make predictions on test data
    y_pred = model.predict(X_test)

    # Add predicted floor area column to test data
    result['floor_area_sf_predicted'] = y_pred

    result.drop(['floor_area_sf'], axis=1, inplace=True)

    return result

    # Save test data with predicted floor area column to CSV
    # test_data.to_csv('./data/test_data_predicted.csv', index=False)

# file3 = './data/testing.csv'
# with open(file3, 'rb') as f:
#     enc3 = chardet.detect(f.read())

# cols = ["OID_"," id", "floor_area_sf", "civic_number"]
# test_data = pd.read_csv(file3, encoding=enc3['encoding'], usecols=cols)

# machine_learning(test_data)