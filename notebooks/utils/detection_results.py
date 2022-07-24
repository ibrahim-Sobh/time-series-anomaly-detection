from sklearn.metrics import f1_score, recall_score, precision_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import pandas as pd
def detection_anomalies(data_df_encod, outlier, normal, sensor,Z):
    plt.figure(figsize=(15,4))
    data_sensor = data_df_encod[sensor]
    data_sensor.plot(alpha=0.5)
    
    anomalies_FP = data_sensor[(Z==outlier) & (data_df_encod['machine_status']==1)]
    if anomalies_FP.size:
        anomalies_FP.plot(marker='X', linestyle='none', c="g", alpha=0.7)

    anomalies_TP = data_df_encod[((data_df_encod['machine_status']==2) | (data_df_encod['machine_status']==0)) & (Z==outlier)][sensor]
    if anomalies_TP.size:
        anomalies_TP.plot(marker='x', linestyle='none', c="b", alpha=0.7)
    
    anomalies_FN = data_df_encod[((data_df_encod['machine_status']==2) | (data_df_encod['machine_status']==0)) & (Z==normal)][sensor]
    if anomalies_FN.size:
        anomalies_FN.plot(marker='x', linestyle='none', c="r", alpha=0.7)
        
    anomalies_TN = data_df_encod[(data_df_encod['machine_status']==1) & (Z==normal)][sensor]
    plt.legend(["TN", "FP", "TP", "FN"])
    plt.show();
    
    plt.figure(figsize=(12,4))
    box = plt.boxplot([data_df_encod[(Z==outlier)][sensor], anomalies_TP, anomalies_FP, anomalies_FN, anomalies_TN ], 
                vert=False, patch_artist=True, labels=["Prediction", "TP","FP", "FN", "TN"])
   
    colors = [ "w", "b", "g", "r", "y"]
    for line, color in zip(box['boxes'], colors):
        line.set(facecolor = color )
        
    plt.show();
    
    return  anomalies_FP, anomalies_TP, anomalies_FN, anomalies_TN

def results_metrics(outlier_label, normal_label, sensor, data_df_encod, y_predicted, anomalies_FP, anomalies_TP, anomalies_FN, anomalies_TN):
    
    anomalies = data_df_encod[data_df_encod['machine_status']!= 1][sensor]
    intersection = anomalies_TP.size
    anomalies_count = anomalies.size
    anomalies_detected = anomalies_FP.size + anomalies_TP.size + anomalies_TN.size
    anomalies_detected_percentage = intersection*100/anomalies_count
    print('Anomalies:', anomalies_count)
    print('Anomalies by Algorithm :', anomalies_detected)
    print('% Anomalies detected: {:.2f}%'. format(anomalies_detected_percentage))

    y_pred = pd.DataFrame(y_predicted).replace({outlier_label:1, normal_label:0})
    y_true = data_df_encod['machine_status'].replace({1:0, 2:1, 0:1})

    TN = anomalies_TN.size
    FP = anomalies_FP.size
    FN = anomalies_FN.size
    TP = anomalies_TP.size

    # false positive rate
    FPR = round(FP/(FP+TN)*100, 2)
    print('False Positive Rate:', FPR)

    # False negative rate
    FNR = round(FN/(TP+FN)*100, 2)
    print('False Negative Rate:', FNR)   

    ACC = round((TP+TN)/(TP+FP+FN+TN)*100, 2)
    
    f1 = round(f1_score(y_true, y_pred, pos_label=outlier_label)*100, 2)
    recall = round(recall_score(y_true, y_pred, pos_label=outlier_label)*100, 2)
    precision = round(precision_score(y_true, y_pred, pos_label=outlier_label)*100, 2)
    print('Accuracy:', ACC) 
    print('F1 Score:', f1) 
    print('Recall:', recall) 
    print('Precision:', precision) 
    
    cnf_matrix=confusion_matrix(y_true, y_pred)
    
    print("")
    print(cnf_matrix)
    print("")
    print(classification_report(y_true, y_pred, zero_division="warn"))
    
    return {'Accuracy': ACC, 'F1': f1, 'Recall':recall, 'Precision': precision,
            'FNR':FNR, 'FPR': FPR,  'anomalies_detected':anomalies_detected,
            'anomalies_detected_percentage':anomalies_detected_percentage,
            'TP_mean':anomalies_TP.mean(), 'FP_mean':anomalies_FP.mean(),
            'FN_mean':anomalies_FN.mean(), 'TN_mean':anomalies_TN.mean(),
            'TP_std':anomalies_TP.std(), 'FP_std':anomalies_FP.std(),
            'FN_std':anomalies_FN.std(), 'TN_std':anomalies_TN.std()}
