import streamlit as st
from datetime import datetime
from src import report
import settings


if __name__ == '__main__':
    date_input:datetime.date  = st.date_input(
        label='Please, choose date',
        min_value=settings.min_date,
        max_value=settings.max_date
    )

    lost_revenue:float = report.sum_daily_lost_revenue_for_date(date_input)
    if lost_revenue is not None:
        st.write(f'Lost Revenue: {lost_revenue}')
    else:
        st.write(f"There's no data for this date: {date_input}")