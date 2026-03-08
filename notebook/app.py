import streamlit as st
import pandas as pd

# Load the association rules
@st.cache_data
def load_rules():
    rules = pd.read_csv("strong_rules.csv")  # make sure this file exists
    rules['antecedents'] = rules['antecedents'].apply(eval)
    rules['consequents'] = rules['consequents'].apply(eval)
    return rules

rules = load_rules()

# Extract unique products from antecedents
product_options = sorted({item for rule in rules['antecedents'] for item in rule})

# Streamlit App UI
st.title("🛒 Product Recommendation System")
st.write("Select a product to view what customers frequently buy next.")

# Dropdown for product selection
selected_product = st.selectbox("Choose a product:", product_options)

# Recommendation function
def recommend_products(item, rules_df, top_n=5):
    filtered = rules_df[rules_df['antecedents'].apply(lambda x: item in x)]
    filtered = filtered.sort_values(by=['confidence', 'lift'], ascending=False)
    return filtered['consequents'].apply(lambda x: list(x)[0]).head(top_n).tolist()

# Show recommendations
if selected_product:
    recommendations = recommend_products(selected_product, rules)
    if recommendations:
        st.success(f"Top recommendations for **{selected_product}**:")
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"{i}. **{rec}**")
    else:
        st.warning("No recommendations found for this product.")
