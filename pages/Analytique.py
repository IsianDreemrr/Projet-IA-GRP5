import streamlit as st
from notebook import execute_all_analyses
import pandas as pd 

def main():
    st.title("Analyse Complète des Données")

    analyses, corr_plot_path, correlations, plot_paths = execute_all_analyses()

    st.write("## Analyses Basiques")
    for analysis, result in analyses.items():
        st.write(f"### {analysis.replace('_', ' ').capitalize()}")
        if isinstance(result, pd.Series) or isinstance(result, pd.DataFrame):
            st.dataframe(result)
        else:
            st.text(result)

    st.write("## Corrélations")
    st.image(corr_plot_path)
    st.dataframe(correlations)

    st.write("## Visualisations")
    for title, path in plot_paths.items():
        st.write(f"### {title.replace('_', ' ').capitalize()}")
        st.image(path)

if __name__ == "__main__":
    main()


# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")