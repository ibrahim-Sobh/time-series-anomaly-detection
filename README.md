# Time Series Anomaly Detection :chart_with_downwards_trend::rotating_light::chart_with_upwards_trend:

## Group:
    
- Isaac Gonzales Vizcarra
- Ibrahim Sobh
- Anthony Siampiringue

## Dataset::potable_water:
    Water pump data predictions Data
    https://www.kaggle.com/datasets/nphantawee/pump-sensor-data
        
## Description:
- Data driven prediction models of water pump sensor.
 

## Anomalies Detection Approaches :scientist:

1. Heuristics based approaches  :man_cook:
    - Cutoff method using Mean and Standard deviation</br> cutoff = mean + upper_cutoff_threshold * std  
    - Global Z-score:</br> Z_score = (x - mean) / std
    - Inter quartile range IQR: </br> [ – 1.5 * IQR , + 1.5 * IQR ]
    - Special Z-score with Sliding Window:</br> ( Local_Z_score + Lambda  * Global_Z-score ) / 2

2.  Gaussian Hidden Markov Model  :technologist:

The Gaussian hidden Markov model (Gaussian HMM) is a type of finite-state-space and homogeneous HMM where the observation probability distribution is the normal distribution (Gaussian).

    Y_t | S_t ~ N(mu_St, sigma_St)

where x_t is the observation at time t, x_1 ... x_t−1 are the observations at time t−1, ..., t−k, and mu_St and sigma_St are the mean and standard deviation of the normal distribution.

3. Local Outlier Factor LOF: :ninja:
<img width="434" alt="Screenshot 2022-07-19 at 7 45 35 PM" src="https://user-images.githubusercontent.com/49615833/179815671-633f946a-be3b-477b-83ae-d9f437e82d96.png">

4. LSTM :robot:

LSTM is a recurrent neural network (RNN) that is designed to process sequences of data. with LSTM, you can process sequences of data in a way that is similar to how you process data in a language. the architecture used is the autoencoder.
          
      

