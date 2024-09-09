def aggregate_experience_data(df):
    experience_data = df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'TCP UL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Avg RTT UL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Avg Bearer TP UL (kbps)': 'mean',
        'Handset Type': 'first'
    })

    experience_data['Avg RTT (ms)'] = (experience_data['Avg RTT DL (ms)'] + experience_data['Avg RTT UL (ms)']) / 2
    experience_data['Avg Throughput (Mbps)'] = (experience_data['Avg Bearer TP DL (kbps)'] + experience_data['Avg Bearer TP UL (kbps)']) / 2000
    experience_data['TCP Retransmission'] = (experience_data['TCP DL Retrans. Vol (Bytes)'] + experience_data['TCP UL Retrans. Vol (Bytes)']) / 2
    
    return experience_data
