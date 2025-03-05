import streamlit as st
import numpy as np

# Function to calculate weighted marks
def calculate_weighted_marks(marks, weight, total_marks):
    return (marks * weight) / total_marks if total_marks != 0 else 0

# Streamlit app
def aggregate_calculator():
    st.title("Aggregate Calculator")

    ssc_marks = st.text_input("Enter SSC marks:", min_value=0)
    ssc_total = st.text_input("Enter total SSC marks:", min_value=0)
    hssc_marks = st.text_input("Enter HSSC marks:", min_value=0)
    hssc_total = st.text_input("Enter total HSSC marks:", min_value=0)
    ba_bsc_marks = st.text_input("Enter BA/BSc marks (leave blank if not applicable):")
    ba_bsc_total = st.text_input("Enter total BA/BSc marks (leave blank if not applicable):")
    bs_marks = st.text_input("Enter BS marks (leave blank if not applicable):")
    bs_total = st.text_input("Enter total BS marks (leave blank if not applicable):")
    ma_msc_marks = st.text_input("Enter MA/MSc marks (leave blank if not applicable):")
    ma_msc_total = st.text_input("Enter total MA/MSc marks (leave blank if not applicable):")
    ade_bed_marks = st.text_input("Enter ADE/BEd marks (leave blank if not applicable):")
    ade_bed_total = st.text_input("Enter total ADE/BEd marks (leave blank if not applicable):")
    med_marks = st.text_input("Enter MEd marks (leave blank if not applicable):")
    med_total = st.text_input("Enter total MEd marks (leave blank if not applicable):")
    mphil_marks = st.text_input("Enter MPhil marks (leave blank if not applicable):")
    mphil_total = st.text_input("Enter total MPhil marks (leave blank if not applicable):")
    phd_marks = st.text_input("Enter PhD marks (leave blank if not applicable):")
    phd_total = st.text_input("Enter total PhD marks (leave blank if not applicable):")

    if st.button("Calculate Aggregate"):
        ssc_weighted = calculate_weighted_marks(ssc_marks, 15, ssc_total)
        hssc_weighted = calculate_weighted_marks(hssc_marks, 20, hssc_total)
        ba_bsc_weighted = calculate_weighted_marks(float(ba_bsc_marks), 20, float(ba_bsc_total)) if ba_bsc_marks and ba_bsc_total else 0
        bs_weighted = calculate_weighted_marks(float(bs_marks), 35, float(bs_total)) if bs_marks and bs_total else 0
        ma_msc_weighted = calculate_weighted_marks(float(ma_msc_marks), 15, float(ma_msc_total)) if ma_msc_marks and ma_msc_total else 0
        ade_bed_weighted = calculate_weighted_marks(float(ade_bed_marks), 15, float(ade_bed_total)) if ade_bed_marks and ade_bed_total else 0
        med_weighted = calculate_weighted_marks(float(med_marks), 5, float(med_total)) if med_marks and med_total else 0
        mphil_weighted = calculate_weighted_marks(float(mphil_marks), 5, float(mphil_total)) if mphil_marks and mphil_total else 0
        phd_weighted = calculate_weighted_marks(float(phd_marks), 5, float(phd_total)) if phd_marks and phd_total else 0

        aggregate = (
            ssc_weighted +
            hssc_weighted +
            ba_bsc_weighted +
            bs_weighted +
            ma_msc_weighted +
            ade_bed_weighted +
            med_weighted +
            mphil_weighted +
            phd_weighted
        )

        st.success(f"The aggregate percentage is: {aggregate:.2f}%")

# Run the Streamlit app
if __name__ == "__main__":
    aggregate_calculator()
