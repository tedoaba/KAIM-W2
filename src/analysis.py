def analyze_top_handsets(df):
    """Identify the top 10 handsets used by customers."""
    return df['Handset Type'].value_counts().head(10)

def analyze_top_manufacturers(df):
    """Identify the top 3 handset manufacturers."""
    return df['Handset Manufacturer'].value_counts().head(3)

def aggregate_application_data(df, app_columns):
    """Aggregate user traffic per application."""
    app_data = df.groupby('MSISDN/Number')[app_columns].sum().reset_index()
    return app_data

def get_top_10_users_per_application(app_data, app_columns):
    """Get the top 10 most engaged users per application."""
    top_users_per_app = pd.melt(app_data, id_vars='MSISDN/Number', value_vars=app_columns,
                                var_name='Application', value_name='Total Traffic (Bytes)')
    return top_users_per_app.groupby('Application').apply(
        lambda x: x.nlargest(10, 'Total Traffic (Bytes)')
    ).reset_index(drop=True)
