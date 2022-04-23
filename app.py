import streamlit as st
from model import run_model

def get_rc_vars(costs_choice):
    if(costs_choice == 'With Cost'):
        return ['Division','LaborHours','PartsCost','LaborCost','PaintMaterialsCost','TowingCost','SubletCost','RentalCost','StateProv','BodyLaborHours', 'PaintLaborHours','FrameLaborHours', 'MechanicalLaborHours', 'OtherLaborHours','ArrivedToDeliveredDays','CollisionROFlagYN','dimDRPFlagYN','PaintFlagYN','TowingFlagYN','VehicleMake','VehicleModel','VehicleCategory']
    else:
        return ['Division','StateProv','LaborHours','ArrivedToDeliveredDays','CollisionROFlagYN','dimDRPFlagYN','PaintFlagYN','TowingFlagYN','VehicleMake','VehicleModel','VehicleCategory']

def get_pmc_vars(costs_choice):
    if(costs_choice == 'With Cost'):
        return ['PartsCost','LaborCost', 'TowingCost','SubletCost','RentalCost','StateProv','LaborHours','ArrivedToDeliveredDays','CollisionROFlagYN','dimDRPFlagYN','PaintFlagYN','TowingFlagYN','VehicleMake','VehicleModel','VehicleCategory']
    else:
        return ['StateProv','LaborHours','ArrivedToDeliveredDays','CollisionROFlagYN','dimDRPFlagYN','PaintFlagYN','TowingFlagYN','VehicleMake','VehicleModel','VehicleCategory']

def main():
    st.title('ClaimsCorps Web App')

    model_choice = st.radio(
        "Which model to run",
        ('Repair Cost', 'Paint Material Cost'))

    costs_choice = st.radio(
        "Do you want to run with or without costs",
        ('With Cost', 'Without Cost'))

    with st.form(key='my_form'):
        col_values = dict()

        if (model_choice == 'Repair Cost'):
            input_vars = get_rc_vars(costs_choice)
            for cols in input_vars:
                col_name = str(cols)
                col_values[col_name] = st.text_input(label=str(cols))
        else:
            input_vars = get_pmc_vars(costs_choice)
            for cols in input_vars:
                col_name = str(cols)
                col_values[col_name] = st.text_input(label=str(cols))

        submit_button = st.form_submit_button(label='Submit')

        if(submit_button):
            prediction = run_model(model_choice, costs_choice, col_values)
            st.subheader("Estimated " + str(model_choice) + ": " + str(prediction))

if __name__ == '__main__':
    main()