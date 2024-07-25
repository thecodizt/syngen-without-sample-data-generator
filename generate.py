import pandas as pd
from methods.numeric import generate_random_noise_with_properties
from methods.categoric import generate_random_strings_with_distribution
from methods.geographic import generate_lat_lon_data
from methods.date import generate_random_date

def generate(configurations):
    tables = []
    
    for config in configurations:
        columns = []
        
        num_records = config["num_records"]
        for col in config["columns"]:
            if col["type"] == "Numeric":
                if config["type"] == "Cross-Sectional":
                    numeric_data = generate_random_noise_with_properties(
                        min_val=col["min"],
                        max_val=col["max"],
                        mean=col["mean"],
                        std_dev=col["std_deviation"],
                        num_samples=num_records
                    )
                    columns.append(numeric_data)
                            
                elif config["type"] == "Time Series":
                    numeric_data = generate_random_noise_with_properties(
                        min_val=col["min"],
                        max_val=col["max"],
                        mean=col["mean"],
                        std_dev=col["std_deviation"],
                        amplitude=col["seasonality"]["amplitude"],
                        frequency=col["seasonality"]["frequency"],
                        slope=col["trend"]["slope"],
                        num_samples=num_records
                    )
                    columns.append(numeric_data)
                        
            elif col["type"] == "Categorical":
                categoric_data = generate_random_strings_with_distribution(
                    num_unique=col["unique_values"],
                    distribution=col["distribution"],
                    num_records=num_records
                )
                
                columns.append(categoric_data)
                
            elif col["type"] == "Geographical":
                geographic_data = generate_lat_lon_data(
                    root_lat=col["lat"],
                    root_lon=col["lon"],
                    lat_radius=col["radius_lat"],
                    lon_radius=col["radius_lon"],
                    n_unique=col["num_unique"],
                    distribution=col["distribution"],
                    num_records=num_records
                )
                
                columns.append(geographic_data)
                
            elif col["type"] == "Date":
                date_data = generate_random_date(
                    start=col["start_date"], 
                    end=col["end_date"], 
                    num_unique=col["num_unique"],
                    distribution=col["distribution"],
                    num_records=num_records
                )          
                
                columns.append(date_data)
        
        formatted_columns = []
        
        for i in range(len(columns)):
            name = config["columns"][i]["name"]
            series = pd.Series(columns[i], name=name)
            formatted_columns.append(series)
    
        table = pd.concat(formatted_columns, axis=1)
        
        if config["type"] == "Time Series":
            table.index = pd.date_range(start=config["start_date"], end=config["end_date"], periods=num_records)
 
        tables.append(table)
        
    return tables