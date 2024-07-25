import streamlit as st
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker

def ui_input():
    
    configuration = []
    
    num_tables = st.number_input("Enter the number of tables", min_value=1, step=1, value=1, key="num_tables")
    
    st.divider()
    
    for i in range(num_tables):
        st.subheader(f"Table {i+1}")
        
        table_name = st.text_input(f"Enter table name {i+1}:", key=f"table_name_{i}")
        table_type = st.selectbox("Select table type:", ("Cross-Sectional", "Time Series"), key=f"table_type_{i}")
        
        start_date = None
        end_date = None    
        
        if table_type == "Time Series":
            st.write("Index Range")
            datetime_string = date_range_picker(picker_type=PickerType.time.string_value,
                                      start=-30, end=0, unit=Unit.minutes.string_value,
                                      key='range_picker'
                                    )
            if datetime_string is not None:
                start_date = datetime_string[0]
                end_date = datetime_string[1]
                    
        num_records = st.number_input(f"Enter the number of records for {table_name}", min_value=1, step=100, value=100, key=f"num_records_{i}")
        
        st.subheader("Columns")
        
        num_columns = st.number_input("Enter the number of columns", min_value=1, step=1, value=1, key=f"num_columns_{i}")

        columns = []
        for j in range(num_columns):

            column_name = st.text_input(f"Enter column name {j + 1}:", key=f"column_name_{i}_{j}")
            column_type = st.selectbox(f"Select column type for {column_name}:", ("Numeric", "Categorical", "Geographical", "Date"), key=f"column_type_{i}_{j}")

            if column_type == "Numeric":
                min_value = st.number_input(f"Enter minimum value for {column_name}:", value=0.0, key=f"min_value_{i}_{j}")
                max_value = st.number_input(f"Enter maximum value for {column_name}:", value=100.0, key=f"max_value_{i}_{j}")
                mean_value = st.number_input(f"Enter mean value for {column_name}:", value=50.0, key=f"mean_value_{i}_{j}")
                std_deviation = st.number_input(f"Enter standard deviation for {column_name}:", value=10.0, key=f"std_deviation_{i}_{j}")
                
                amplitude = 1
                frequency = 1
                slope = 0
                
                if table_type == "Time Series":
                    with st.expander(f"Options for Numeric Column {column_name}"):
                        col_seasonality = st.checkbox(f"Add Seasonality to {column_name}?", key=f"col_seasonality_{i}_{j}")

                        if col_seasonality:
                            amplitude = st.number_input(f"Enter Seasonality Amplitude for {column_name}:", key=f"amplitude_{i}_{j}")
                            frequency = st.number_input(f"Enter Seasonality Frequency for {column_name}:", key=f"frequency_{i}_{j}")
                        
                        col_trend = st.checkbox(f"Add Trend to {column_name}?", key=f"col_trend_{i}_{j}")
                        
                        if col_trend:
                            slope = st.number_input(f"Enter Trend Slope for {column_name}:", key=f"slope_{i}_{j}")

                columns.append({"name": column_name, "type": column_type, 
                                "min": min_value, "max": max_value, "mean": mean_value, "std_deviation": std_deviation,
                                "seasonality": {"amplitude": amplitude, "frequency": frequency},
                                "trend": {"slope": slope}})
                
            elif column_type == "Categorical":
                unique_values = st.number_input(f"Enter number of unique categorical values for {column_name}:", min_value=1, max_value=num_records)
                distribution = st.selectbox("Select the expected frequency distribution: ", ["Uniform", "Normal", "Exponential"])
                columns.append({"name": column_name, "type": column_type, "unique_values": unique_values, "distribution": distribution})
                
            elif column_type == "Geographical":
                lat = st.number_input(f"Root Latitude for {column_name}: ", min_value=-90.0, max_value=90.0, step=0.01, value=0.0)
                lon = st.number_input(f"Root Longitude for {column_name}: ", min_value=-180.0, max_value=180.0, step=0.01, value=0.0)
                radius_lat = st.number_input(f"Latitude radius for {column_name}: ", min_value=0, max_value=90)
                radius_lon = st.number_input(f"Longitude radius for {column_name}: ", min_value=0, max_value=180)
                num_unique = st.number_input(f"Number of unique geographical points for {column_name}: ", min_value=1, max_value=num_records)
                distribution = st.selectbox("Select the expected frequency distribution: ", ["Uniform", "Normal", "Exponential"], key=f'dist_geo_{i}')
                columns.append({"name": column_name, "type": column_type, "lat": lat, "lon": lon, "radius_lat": radius_lat, "radius_lon": radius_lon, "num_unique": num_unique, "distribution": distribution})
            
            elif column_type == "Date":
                start = None
                end = None
                
                st.write("Enter date range: ")
                datetime_string = date_range_picker(picker_type=PickerType.time.string_value,
                                      start=-30, end=0, unit=Unit.minutes.string_value,
                                      key=f'range_picker_{i}_{j}'
                                    )
                num_unique = st.number_input(f"Number of unique date points for {column_name}: ", min_value=1, max_value=num_records)
                distribution = st.selectbox("Select the expected frequency distribution: ", ["Uniform", "Normal", "Exponential"], key=f'dist_date_{i}')
                
                if datetime_string is not None:
                    start = datetime_string[0]
                    end = datetime_string[1]
                    
                    columns.append({"name": column_name, "type": column_type, "start_date": start, "end_date": end, "num_unique": num_unique, "distribution": distribution})
                    
            else:
                columns.append({"name": column_name, "type": column_type})
            
        configuration.append({"name": table_name, "type": table_type, "columns": columns, "num_records": num_records, "start_date": start_date, "end_date": end_date})
        
        st.divider()
        
    return configuration

def config_input():
    pass