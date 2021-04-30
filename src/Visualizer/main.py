import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasgui import show

def sortDataframe(raw_df, filter_direction):
    df= raw_df.loc[(raw_df["direction"] == filter_direction) & (raw_df["id"] <= 200)]
    df.reset_index(drop=True, inplace=True)
    return df

def main():
    #SigGen
    df_gen_run1 = sortDataframe(pd.read_csv("run1_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_gen_run2 = sortDataframe(pd.read_csv("run2_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_gen_run3 = sortDataframe(pd.read_csv("run3_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_gen_run4 = sortDataframe(pd.read_csv("run4_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")

   #Moving Average
    df_mavg_out_run2 = sortDataframe(pd.read_csv("run2_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_mavg_out_run3 = sortDataframe(pd.read_csv("run3_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_mavg_out_run1 = sortDataframe(pd.read_csv("run1_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_mavg_out_run4 = sortDataframe(pd.read_csv("run4_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")

    df_mavg_in_run2 = sortDataframe(pd.read_csv("run2_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_mavg_in_run3 = sortDataframe(pd.read_csv("run3_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_mavg_in_run1 = sortDataframe(pd.read_csv("run1_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_mavg_in_run4 = sortDataframe(pd.read_csv("run4_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

    #Func
    df_func_out_run1 = sortDataframe(pd.read_csv("run1_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_func_out_run2 = sortDataframe(pd.read_csv("run2_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_func_out_run3 = sortDataframe(pd.read_csv("run3_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")
    df_func_out_run4 = sortDataframe(pd.read_csv("run4_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "OUT")

    df_func_in_run1 = sortDataframe(pd.read_csv("run1_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_func_in_run3 = sortDataframe(pd.read_csv("run3_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_func_in_run2 = sortDataframe(pd.read_csv("run2_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_func_in_run4 = sortDataframe(pd.read_csv("run4_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

    #Client
    df_client_run1 = sortDataframe(pd.read_csv("run1_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]) , "IN")
    df_client_run2 = sortDataframe(pd.read_csv("run2_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_client_run3 = sortDataframe(pd.read_csv("run3_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")
    df_client_run4 = sortDataframe(pd.read_csv("run4_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

    #Delay1
    df_gen_delay1 =  sortDataframe(pd.read_csv("delay1_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])    , "OUT")
    df_mavg_out_delay1 = sortDataframe(pd.read_csv("delay1_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_func_out_delay1 = sortDataframe(pd.read_csv("delay1_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_mavg_in_delay1 = sortDataframe(pd.read_csv("delay1_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_func_in_delay1 = sortDataframe(pd.read_csv("delay1_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_client_delay1 =sortDataframe(pd.read_csv("delay1_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

     #Delay2
    df_gen_delay2 =  sortDataframe(pd.read_csv("delay2_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])    , "OUT")
    df_mavg_out_delay2 = sortDataframe(pd.read_csv("delay2_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_func_out_delay2 = sortDataframe(pd.read_csv("delay2_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_mavg_in_delay2 = sortDataframe(pd.read_csv("delay2_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_func_in_delay2 = sortDataframe(pd.read_csv("delay2_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_client_delay2 =sortDataframe(pd.read_csv("delay2_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

     #Delay3
    df_gen_delay3 =  sortDataframe(pd.read_csv("delay3_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])    , "OUT")
    df_mavg_out_delay3 = sortDataframe(pd.read_csv("delay3_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_func_out_delay3 = sortDataframe(pd.read_csv("delay3_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_mavg_in_delay3 = sortDataframe(pd.read_csv("delay3_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_func_in_delay3 = sortDataframe(pd.read_csv("delay3_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_client_delay3 =sortDataframe(pd.read_csv("delay3_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

    #Delay4
    df_gen_delay4 = sortDataframe(pd.read_csv("delay4_gen_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])    , "OUT")
    df_mavg_out_delay4 = sortDataframe(pd.read_csv("delay4_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_func_out_delay4 = sortDataframe(pd.read_csv("delay4_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "OUT")
    df_mavg_in_delay4 = sortDataframe(pd.read_csv("delay4_mavg_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_func_in_delay4 = sortDataframe(pd.read_csv("delay4_func_output.csv", header=0, names=["timestamp", "direction", "topic", "id"])   , "IN")
    df_client_delay4 = sortDataframe(pd.read_csv("delay4_client_output.csv", header=0, names=["timestamp", "direction", "topic", "id"]), "IN")

    experiment1 = pd.DataFrame()
    experiment1["run1_t_mavg"] = df_mavg_out_run1["timestamp"] - df_mavg_in_run1["timestamp"]
    experiment1["run1_t_func"] = df_func_out_run1["timestamp"] - df_func_in_run1["timestamp"]
    experiment1["run1_t_tot"] = df_client_run1["timestamp"] - df_gen_run1["timestamp"]
    experiment1["run2_t_mavg"] = df_mavg_out_run2["timestamp"] - df_mavg_in_run2["timestamp"]
    experiment1["run2_t_func"] = df_func_out_run2["timestamp"] - df_func_in_run2["timestamp"]
    experiment1["run2_t_tot"] = df_client_run2["timestamp"] - df_gen_run2["timestamp"]
    experiment1["run3_t_mavg"] = df_mavg_out_run3["timestamp"] - df_mavg_in_run3["timestamp"]
    experiment1["run3_t_func"] = df_func_out_run3["timestamp"] - df_func_in_run3["timestamp"]
    experiment1["run3_t_tot"] = df_client_run3["timestamp"] - df_gen_run3["timestamp"]
    experiment1["run4_t_mavg"] = df_mavg_out_run4["timestamp"] - df_mavg_in_run4["timestamp"]
    experiment1["run4_t_func"] = df_func_out_run4["timestamp"] - df_func_in_run4["timestamp"]
    experiment1["run4_t_tot"] = df_client_run4["timestamp"] - df_gen_run4["timestamp"]
    exp1_mean = (experiment1.mean(axis=0))

    experiment2 = pd.DataFrame()
    experiment2["delay750_t_mavg"] = df_mavg_out_delay1["timestamp"] - df_mavg_in_delay1["timestamp"]
    experiment2["delay750_t_func"] = df_func_out_delay1["timestamp"] - df_func_in_delay1["timestamp"]
    experiment2["delay750_t_tot"] = df_client_delay1["timestamp"] - df_gen_delay1["timestamp"]
    experiment2["delay500_t_mavg"] = df_mavg_out_delay2["timestamp"] - df_mavg_in_delay2["timestamp"]
    experiment2["delay500_t_func"] = df_func_out_delay2["timestamp"] - df_func_in_delay2["timestamp"]
    experiment2["delay500_t_tot"] = df_client_delay2["timestamp"] - df_gen_delay2["timestamp"]
    experiment2["delay250_t_mavg"] = df_mavg_out_delay3["timestamp"] - df_mavg_in_delay3["timestamp"]
    experiment2["delay250_t_func"] = df_func_out_delay3["timestamp"] - df_func_in_delay3["timestamp"]
    experiment2["delay250_t_tot"] = df_client_delay3["timestamp"] - df_gen_delay3["timestamp"]
    experiment2["delay50_t_mavg"] = df_mavg_out_delay4["timestamp"] - df_mavg_in_delay4["timestamp"]
    experiment2["delay50_t_func"] = df_func_out_delay4["timestamp"] - df_func_in_delay4["timestamp"]
    experiment2["delay50_t_tot"] = df_client_delay4["timestamp"] - df_gen_delay4["timestamp"]
    exp2_mean = (experiment2.mean(axis=0))

    axes = plt.gca()
    axes.set_ylim([0, 60])

    #Comment the two following lines depending on which experiment should be plotted
    #exp1_mean.plot(kind="bar")
    exp2_mean.plot(kind="bar")

    plt.show()

if __name__ == '__main__':
    main()