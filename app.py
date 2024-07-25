import streamlit as st

from inputs import ui_input, config_input
from generate import generate
from visualize import visualize

def without_sample_data_generator():
    st.title("Without Sample Data Generator")
    
    with st.expander("Documentaion"):
        st.markdown("""
            # TBD            
        """)
        
    st.header("Configurations")
    
    # input_option = st.selectbox(
    #     'How do you want to enter the data generation configuration?',
    #     ('UI', 'Config File (YAML)')
    # )
    
    input_option = 'UI'
    
    configuration = None
    
    if input_option == "UI":
        configuration = ui_input()
    else:
        configuration = config_input()
        
    if configuration: 
        st.subheader("Configuration")
        
        st.write(configuration)
        
    is_generate = st.button("Generate")
    
    st.divider()
    
    tables = []
    
    if is_generate and configuration is not None:
        tables = generate(configuration)
        
    if tables:
        for i in range(len(tables)):
            st.header(f"Table {i+1}")
            
            st.subheader("Configuration")
            st.write(configuration[i], key={i})
            
            st.subheader("Data")
            st.dataframe(tables[i])
            
            st.subheader("Visualization")
            visualize(table=tables[i])
            
            st.subheader("Download")
            csv_file = tables[i].to_csv(index=False).encode('utf-8')
            st.download_button(f"Download {configuration[i]['name']} as CSV", csv_file, f'{configuration[i]["name"]}_data.csv', 'text/csv', key={i})
            
            st.divider()
            
if __name__ == "__main__":
    without_sample_data_generator()